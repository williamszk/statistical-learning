# Just some notes on comparing performance of servers.

Compare server performance

- In Python we can run the server in debug mode in local computer.
- We'll use a json file to include the fields that we'll need to control the 
conditions of the experiment.
- What are the fields that we'll need?

- "location": ["local machine", "ec2 instance", "load-balancer"]
- "web-framework": ["python-flask", "rust-actix", ...]
- "analysis-tool": "autocannon"
what are other http analysis tools?
There is a tool in go for testing http endpoints

We could just use curl for testing an endpoint

We could try using "Siege"

{
    "server-location":"local-machine", 
    "" 
}

- Can we run go executables directly without a load balancer?
- What is the function of gunicorn?
- What are alternatives to guinicorn?

---

Testing Go fiber and flask in debug mode showed that both have a pretty close
performance using curl to get the request time lapse.

The performance bottle neck must be on the client tool.

I need to find another tool to test.

I tested with autocannon, but it gave me the same result with all zeros values.

---

Solved the problem with autocannon.

The problem was that I was writing: 

`autocannon -c 100 -d 5 -p 10 http://localhost:5000/`

And it should be:

`autocannon -c 100 -d 5 -p 10 http://127.0.0.1:5000/`

---

Below is the result for Go fiber:

```txt
Running 5s test @ http://127.0.0.1:5000/ 
100 connections with 10 pipelining factor

┌─────────┬───────┬───────┬───────┬───────┬──────────┬─────────┬────────┐
│ Stat    │ 2.5%  │ 50%   │ 97.5% │ 99%   │ Avg      │ Stdev   │ Max    │
├─────────┼───────┼───────┼───────┼───────┼──────────┼─────────┼────────┤
│ Latency │ 15 ms │ 16 ms │ 19 ms │ 26 ms │ 16.07 ms │ 6.48 ms │ 215 ms │
└─────────┴───────┴───────┴───────┴───────┴──────────┴─────────┴────────┘
┌───────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
│ Stat      │ 1%      │ 2.5%    │ 50%     │ 97.5%   │ Avg     │ Stdev   │ Min     │
├───────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│ Req/Sec   │ 58591   │ 58591   │ 62943   │ 71871   │ 63840   │ 4340.67 │ 58560   │
├───────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│ Bytes/Sec │ 6.91 MB │ 6.91 MB │ 7.43 MB │ 8.48 MB │ 7.53 MB │ 511 kB  │ 6.91 MB │
└───────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘

Req/Bytes counts sampled once per second.
# of samples: 5

320k requests in 5.33s, 37.7 MB read 
```

Below is the result for flask using the debug, not production with gunicorn

```txt
$ autocannon -c 100 -d 5 -p 10 http://127.0.0.1:5000/
Running 5s test @ http://127.0.0.1:5000/
100 connections with 10 pipelining factor

┌─────────┬───────┬───────┬────────┬────────┬─────────┬──────────┬────────┐
│ Stat    │ 2.5%  │ 50%   │ 97.5%  │ 99%    │ Avg     │ Stdev    │ Max    │
├─────────┼───────┼───────┼────────┼────────┼─────────┼──────────┼────────┤
│ Latency │ 55 ms │ 86 ms │ 130 ms │ 131 ms │ 88.1 ms │ 25.13 ms │ 131 ms │
└─────────┴───────┴───────┴────────┴────────┴─────────┴──────────┴────────┘
┌───────────┬─────┬──────┬─────┬─────────┬─────────┬─────────┬─────────┐
│ Stat      │ 1%  │ 2.5% │ 50% │ 97.5%   │ Avg     │ Stdev   │ Min     │
├───────────┼─────┼──────┼─────┼─────────┼─────────┼─────────┼─────────┤
│ Req/Sec   │ 0   │ 0    │ 0   │ 100     │ 20      │ 40      │ 100     │
├───────────┼─────┼──────┼─────┼─────────┼─────────┼─────────┼─────────┤
│ Bytes/Sec │ 0 B │ 0 B  │ 0 B │ 18.4 kB │ 3.68 kB │ 7.36 kB │ 18.4 kB │
└───────────┴─────┴──────┴─────┴─────────┴─────────┴─────────┴─────────┘

Req/Bytes counts sampled once per second.
# of samples: 5

1k requests in 5.07s, 18.4 kB read
```

With just this example we see that Go fiber as it is is pretty fast.
The median is 16ms. The Flask with debug which is not a fair comparison
is 86ms.

---

All the answer below from chat gpt.

For Go fiber can we just use the executable without the need to have a
load balancer?

```txt
Yes, you can use an executable created with Go fiber without the need for a load balancer. Go fiber is a lightweight and fast web framework for Go language, and it is designed to be able to handle multiple requests simultaneously, making it suitable for high-performance applications.

However, if you have multiple instances of the Go fiber executable running on different machines, you may want to consider using a load balancer to distribute the incoming traffic evenly across those instances. This can help improve the overall performance and reliability of your application.

Additionally, if you are planning to deploy your application to a cloud provider such as AWS, GCP, or Azure, they typically provide load balancing services that you can use to distribute traffic to your application instances. In this case, you would not need to set up your own load balancer.
```

Can I use a go fiber executable in production? Or should I use some other method for setting a
go fiber application in production?

```txt
Yes, you can use a Go fiber executable in production. In fact, Go fiber is designed to be a production-ready web framework, and many companies use it in their production systems. However, there are some additional steps you should take to ensure your application is ready for production.

Here are some things you should consider when deploying your Go fiber application to production:

Use HTTPS: Always use HTTPS to encrypt communication between the client and server. You can use a tool like Let's Encrypt to get a free SSL/TLS certificate.

Set environment variables: Use environment variables to store sensitive information such as database credentials or API keys. Do not hardcode these values in your code.

Use logging: Implement logging to keep track of errors and important events in your application.

Set up monitoring: Use a monitoring tool such as Prometheus or Grafana to monitor the health of your application and the performance of your servers.

Deploy with a process manager: Use a process manager like systemd or supervisor to manage your application as a service, and ensure it automatically restarts in case of crashes or server reboots.

Use a reverse proxy: Consider using a reverse proxy like Nginx or Apache to handle load balancing, caching, and serving static files.

By following these best practices, you can ensure your Go fiber application is ready for production and can handle high traffic and load.
```

Does a load balancer improves performance of the server?

```txt
Yes, a load balancer can improve the performance of a server in several ways:

Distributing traffic: A load balancer distributes incoming traffic across multiple servers, allowing them to share the load. This can prevent any one server from becoming overloaded and can improve overall application performance and availability.

Reducing downtime: Load balancers can monitor the health of servers and automatically remove any that are not responding or are experiencing issues. This helps to reduce downtime and ensure that users can always access your application.

Improving scalability: Load balancers make it easier to add or remove servers as needed. This means you can quickly and easily scale your application to handle increased traffic or demand.

Enabling SSL offloading: SSL encryption can be computationally expensive for servers. A load balancer can offload SSL encryption to a separate device, freeing up server resources to focus on serving content and improving performance.

Caching: Some load balancers have built-in caching capabilities. By caching frequently accessed content, a load balancer can reduce the load on servers and improve performance for users.

Overall, using a load balancer can help to improve the performance and availability of your servers, making your application faster and more reliable for users.
```

What is the purpose of using gunicorn when deploying a flask app?

```txt
Gunicorn (short for Green Unicorn) is a Python Web Server Gateway Interface (WSGI) HTTP server that is commonly used to deploy Flask applications. The primary purpose of using Gunicorn is to provide a production-ready server that can handle concurrent requests from multiple clients efficiently and securely.

When a Flask application is run using the built-in Flask development server, it can only handle a single request at a time, which makes it unsuitable for production environments where multiple clients may be accessing the application simultaneously. Gunicorn solves this problem by creating multiple worker processes that can handle requests concurrently, while also providing features like graceful restarts and error handling.

Gunicorn is designed to work seamlessly with popular web servers like Nginx and Apache, allowing you to scale your Flask application horizontally across multiple servers if needed. Additionally, Gunicorn provides options to configure worker processes, threads, and other server parameters, giving you fine-grained control over the performance and behavior of your application.

In summary, using Gunicorn to deploy a Flask application provides a reliable, secure, and scalable solution for serving web applications in a production environment.
```

How to use gunicorn with a proxy server like Nginx?
