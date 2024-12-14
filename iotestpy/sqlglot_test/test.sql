
select 'day' as type, date_trunc('day', timestamp '2024-11-14')
union
select 'week' as type, date_trunc('week', date '2024-11-14')
union
select 'month' as type, date_trunc('month', date '2024-11-14')