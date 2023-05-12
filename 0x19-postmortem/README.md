POSTMORTEM: Two-Hour Outage on May 11, 2023

Issue Summary:
On May 11, 2023, between 3:00 PM and 5:00 PM EST, users of our online marketplace experienced a two-hour outage that prevented them from accessing the website. The outage impacted 100% of our users, resulting in a total loss of revenue during the period.

Timeline:

3:00 PM: The outage was detected through monitoring alerts triggered by a significant increase in server errors.

3:05 PM: An engineer on-call investigated the issue and noticed that the servers were running at full capacity, with the CPU utilization rate exceeding 95%.

3:10 PM: The engineer assumed that the issue was caused by a sudden increase in user traffic and attempted to optimize the servers by adjusting the load balancer settings.

3:20 PM: The optimization attempt failed, and the engineer began to investigate other possible causes, including misconfigured servers and database issues.

4:00 PM: After several misleading paths, the engineer escalated the incident to the database team, suspecting a database performance issue.

4:30 PM: The database team identified the root cause as an inefficient query that was causing the database to lock up.

4:40 PM: The database team fixed the inefficient query by adding an index, and the incident was resolved.

5:00 PM: The website was fully functional again.

Root Cause and Resolution:

The root cause of the outage was an inefficient query that was executed frequently, causing the database to lock up and unable to serve requests. The database team resolved the issue by adding an index to the table, which significantly improved the query performance.

Corrective and Preventative Measures:

To prevent similar incidents from happening in the future, we will take the following corrective and preventative measures:

-Implement a database monitoring system that tracks query performance and flags inefficient queries.

-Perform regular database performance tuning to identify and address performance bottlenecks.

-Conduct a code review to identify and fix any code that might be causing database performance issues.

-Establish a communication protocol for incident escalation to ensure that the right team members are involved in resolving the issue promptly.

-Conduct a post-incident review to identify areas of improvement and implement changes to prevent future incidents.

Tasks as we to do:

-Implement a database monitoring system by May 31, 2023.

-Perform a database performance tuning by June 30, 2023.

-Conduct a code review by July 15, 2023.

-Establish a communication protocol for incident escalation by July 31, 2023.

-Conduct a post-incident review by August 15, 2023, and implement changes accordingly.

In conclusion, we apologize for the inconvenience caused by the outage, and we are committed to improving our systems to prevent future incidents. By taking corrective and preventative measures, we aim to ensure that our online marketplace remains accessible and reliable for our users.
