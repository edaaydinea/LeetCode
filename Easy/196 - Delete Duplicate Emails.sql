delete
from Person
where id NOT in (
    select minimum_ids
    from (
             select min(id) as minimum_ids
             from person
             group by email) as t
)