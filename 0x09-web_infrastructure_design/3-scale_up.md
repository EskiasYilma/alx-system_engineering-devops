# 0-simple_web_stack
---
![](https://github.com/EskiasYilma/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/3-scale_up.png)
---

## Infrastructure Specifics
```
    Why are we adding additional elements?

    Load-balancer:
    The load-balancer is added to distribute traffic between multiple servers, increasing the overall
     capacity and availability of the system. In this case, the load-balancer is configured as a cluster
      with another load-balancer, which adds redundancy and further increases availability.

    Split components:
    Splitting the components into their own servers allows for greater flexibility and scalability.
    For example, if the web server is receiving a lot of traffic, more resources can be allocated to
    that server without affecting the performance of the other components.

    Additional server:
    Adding an additional server provides redundancy and fault tolerance. If one server goes down,
    the other server can take over its responsibilities, ensuring that the system remains operational.
```
