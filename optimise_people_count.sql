


select f.flight_nr,  IFNULL( results.nr_customers,0)
from flights f 
Left Join (WITH summary AS(
			Select  *,
			ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY depart_time ASC) AS rnk
  		    from flights FL LEFT JOIN customer_arrival CA
			on FL.start_loc = CA.arrived_at 
		    AND FL.end_loc = CA.depart_to 
            where FL.depart_time  >= CA.arrival_time
	            )
select  flight_nr, count(customer_id) as  nr_customers
	    from summary
        WHERE summary.rnk = 1
		group by flight_nr) results
        on f.flight_nr = results. flight_nr
        group by flight_nr ORDER BY flight_nr