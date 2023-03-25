# 0-simple_web_stack
---
![](https://github.com/EskiasYilma/alx-system_engineering-devops/blob/b547ade43924fce7c08385d37552ff1c8f873118/0x09-web_infrastructure_design/0-simple_web_stack.png)
---


## Infrastructure Specifics
```
    - Server: A server is a computer system that provides services to other computers or devices connected to it over a network. In this case, the server will host the website and serve web pages to users who access it.

    - Domain name: A domain name is a human-readable label that is used to identify a website on the internet. The role of the domain name is to provide a unique and memorable name for the website that can be used by users to access it.

    - DNS record: The www record in www.foobar.com is a type of DNS record called a subdomain. It is used to indicate that the website is hosted on the www subdomain of the foobar.com domain.

    - Web server: The web server is a software application that receives requests from clients (users) and serves web pages in response. In this infrastructure, Nginx will be used as the web server.

    - Application server: The application server is a software application that executes the application code and generates dynamic content that is served by the web server. In this infrastructure, the application server will be used to execute the code base for the website.

    - Database: The database is a software application that stores and manages data that is used by the application. In this infrastructure, MySQL will be used as the database.

    - Communication: When a user requests the website, the server will communicate with the user's computer over the internet using the HTTP protocol.
```

## Infrastructure Issues
```
    - SPOF: This infrastructure has a single point of failure (SPOF), which means that if the server fails, the website will become unavailable. To mitigate this issue, a backup server or load balancer can be added to the infrastructure.

    - Downtime during maintenance: When deploying new code, the web server needs to be restarted, which will cause the website to become temporarily unavailable. To mitigate this issue, a maintenance page can be displayed during downtime or the deployment can be done during low-traffic periods.

    - Cannot scale: If the website experiences a high volume of incoming traffic, the infrastructure may not be able to handle the load. To mitigate this issue, the infrastructure can be scaled horizontally by adding more servers or vertically by upgrading the server hardware.
```
