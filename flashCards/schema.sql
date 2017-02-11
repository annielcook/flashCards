drop table if exists contact;
create table contact (
	name text not null,
	username text foriegn key not null,
	email text not null
);
