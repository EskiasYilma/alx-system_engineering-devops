# 0-simple_web_stack
---
![](https://github.com/EskiasYilma/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure.png)
---

## Infrastructure Specifics
```
    Why are we adding additional elements?

    - 3 firewalls:
    To enhance the security of the infrastructure and protect against potential attacks from the internet.
    - 1 SSL certificate:
    To serve www.foobar.com over HTTPS, which encrypts traffic between the user's web browser
    and the web server, providing additional security for users.
    - 3 monitoring clients:
    To monitor the performance and health of the infrastructure and alert us to any issues that arise.

    What are firewalls for?
    Firewalls are a security measure that can be used to restrict incoming and outgoing network
    traffic based on a set of predefined rules. They can help protect against unauthorized access
    to the network and prevent malicious traffic from reaching the web server.

    Why is the traffic served over HTTPS?
    Serving traffic over HTTPS encrypts the data between the user's web browser and the web server,
    making it more difficult for attackers to intercept and read sensitive information such as login
    credentials, credit card numbers, and other private data. It also helps protect against certain
    types of attacks, such as man-in-the-middle attacks.

    What monitoring is used for?
    Monitoring is used to track the performance and health of the infrastructure, including web servers,
    application servers, and databases. It helps to identify issues before they become critical,
    and enables quick detection and resolution of any problems that do arise.

    How the monitoring tool is collecting data:
    The monitoring tool is collecting data by running agents on each server in the infrastructure.
    These agents collect metrics such as CPU usage, memory usage, disk usage, network traffic, and
    other system-level statistics. The data is then transmitted to a centralized location where it
    can be analyzed and visualized in real-time.

    Explain what to do if you want to monitor your web server QPS:
    To monitor the QPS (queries per second) of a web server, we would need to collect metrics related
    to web server traffic. This might include information such as the number of requests per second,
    the number of successful responses per second, and the response time for each request. To collect
    this data, a monitoring tool such as Prometheus or Grafana, which can be configured to collect data
    from a variety of sources including web servers, load balancers, and databases, can be used. Once
    the data is collected, we can analyze it to identify trends and potential performance issues, and
    take steps to address them if necessary.
```

## Infrastructure Issues
```
    Terminating SSL at the load balancer level:
    While terminating SSL at the load balancer can reduce the processing load on backend servers, it
    can also introduce security risks. This is because the decrypted traffic is transmitted between
    the load balancer and the backend servers in plain text, which could be intercepted and read by
    attackers. It's generally recommended to be security-centric and encrypt traffic end-to-end whenever
    possible to minimize the risk of data theft.

    Single MySQL server for writes:
    If the single MySQL server that is capable of accepting writes fails, or if it experiences high
    traffic, it could become a bottleneck for the entire application. In addition, if the server fails
    and there is no backup server in place, the entire system could go down. It's generally recommended
    to set up a MySQL cluster with multiple read and write nodes to distribute the load and provide redundancy.

    Identical server components:
    Having all servers with the same components (e.g. identical database, web server, and application
    server software) can lead to several issues. Firstly, it can be difficult to troubleshoot issues
    if they arise since all servers have the same software stack. Secondly, it can make the entire
    system more vulnerable to security threats since any exploit that can take down one server can
    potentially take down all servers. It's generally recommended to use different software versions
    and configurations across servers to provide better isolation and resiliency.

```
