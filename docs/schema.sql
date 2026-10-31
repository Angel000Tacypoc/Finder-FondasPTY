-- Esquema inicial para PostgreSQL/Supabase despues de validar el MVP con JSON.

create type user_role as enum ('user', 'owner', 'moderator', 'admin');
create type place_status as enum ('pending', 'published', 'rejected', 'inactive');
create type report_status as enum ('open', 'reviewing', 'resolved', 'dismissed');

create table profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  display_name text not null,
  role user_role not null default 'user',
  created_at timestamptz not null default now()
);

create table places (
  id bigint generated always as identity primary key,
  name text not null,
  description text not null default '',
  neighborhood text not null,
  latitude numeric(9, 6),
  longitude numeric(9, 6),
  price_range text not null check (price_range in ('$', '$$', '$$$')),
  average_price numeric(10, 2),
  menu jsonb not null default '[]'::jsonb,
  status place_status not null default 'pending',
  owner_id uuid references profiles(id),
  created_by uuid references profiles(id),
  verified_at timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index places_public_search on places (status, neighborhood, price_range);

create table place_reports (
  id bigint generated always as identity primary key,
  place_id bigint not null references places(id) on delete cascade,
  reporter_id uuid references profiles(id),
  reason text not null check (reason in ('closed', 'price_changed', 'menu_changed', 'wrong_data', 'other')),
  details text not null default '',
  status report_status not null default 'open',
  resolved_by uuid references profiles(id),
  created_at timestamptz not null default now(),
  resolved_at timestamptz
);

create table moderation_actions (
  id bigint generated always as identity primary key,
  place_id bigint references places(id) on delete cascade,
  report_id bigint references place_reports(id) on delete cascade,
  moderator_id uuid not null references profiles(id),
  action text not null check (action in ('approve', 'reject', 'request_changes', 'resolve', 'dismiss')),
  notes text not null default '',
  created_at timestamptz not null default now(),
  check (place_id is not null or report_id is not null)
);
