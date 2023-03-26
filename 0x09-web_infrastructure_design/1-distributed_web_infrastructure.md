# 1-distributed_web_infrastructure
---
![](https://github.com/EskiasYilma/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure.png)
---

## Infrastructure Specifics
```
    - Additional servers:
    In a three-server web infrastructure, we add two more servers to distribute
    the load and increase reliability. Having multiple servers ensures that the website can handle a
    large number of requests and can continue running even if one server fails.

    - Load balancer:
    We add a load balancer (HAproxy) to distribute incoming requests across the
    multiple servers in a way that optimizes resource utilization and minimizes response time. The
    distribution algorithm used in this case is round-robin, which distributes requests evenly across
    all available servers. Round-robin algorithm works by taking turns sending requests to each server
    in turn until all servers have received a request, and then starts again from the first server.

    - Active-Active vs Active-Passive setup:
    In this setup, we are using an Active-Active setup, which
    means that both the primary and replica databases are actively serving requests. In an Active-Passive
    setup, only the primary database is actively serving requests, while the replica database is in standby
    mode, waiting to take over if the primary database fails. The advantage of an Active-Active setup is
    that it can handle more load, as both databases can serve requests simultaneously. However, it requires
    more complex synchronization between the databases to ensure data consistency.

    - Primary-Replica database cluster:
    In this setup, we are using a Primary-Replica (Master-Slave)
    database cluster. In this type of cluster, the primary node receives all write requests and replicates
    them to the replica nodes. The replica nodes receive all read requests, and they can also be used to
    promote to the primary node in case of a failure. This setup provides high availability and data
    redundancy, as data is stored on multiple nodes.

    - Primary vs Replica nodes:
    The primary node is responsible for handling all write requests,
    ensuring data consistency across all nodes, and replicating data to the replica nodes. The replica
    nodes are responsible for handling read requests and can be promoted to the primary node in case of
    a failure. In terms of the application, the primary node is where all the writes are directed, and
    the replica nodes are used for reading data. However, the application can be configured to direct
    writes to any node in the cluster, and the database will ensure data consistency by replicating writes to all nodes.
```

## Infrastructure Issues
```
    Single Points of Failure (SPOF):
    The current infrastructure has a single load balancer, which is a SPOF. If the load balancer
    fails, the entire system will be inaccessible to users. Similarly, the use of a single database
    server also creates a SPOF. If the database server fails, the entire system will be unable to provide any data-driven functionality.

    Security issues:
    The infrastructure lacks proper security measures, such as a firewall or HTTPS. This leaves it
    vulnerable to attacks such as DDoS, SQL injection, and other forms of malicious activity. Without
    proper security measures, sensitive user data could also be compromised.

    No monitoring:
    There are no monitoring tools or mechanisms in place to detect and address issues such as high
    traffic or server failures. This lack of monitoring makes it difficult to identify and resolve
    issues before they have a significant impact on the system's availability or performance.
```
