---
title: "Helloworld"
linkTitle: "Helloworld"
weight: 3
bookFlatSection: true
---
# [Helloworld](#Helloworld)



>  **Package : spaceone.api.sample.v1**

<br>
<br>

## Helloworld

The greeting service definition.



**HelloWorld Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**say_hello**](./HelloWorld#say_hello) | [HelloRequest](HelloWorld#hellorequest) | [HelloReply](./HelloWorld#helloreply) |



    
<br>

### say_hello

Sends a greeting







 {{< tabs " say_hello " >}}

 {{< tab "Request Example" >}}



[HelloRequest](./HelloWorld#hellorequest)

* **name** (string)  `Required` 





{{< highlight json >}}
The request message containing the user's name.
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[HelloReply](#HELLOREPLY)
* **message** (string)  `Required` 



{{< highlight json >}}
The response message containing the greetings
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    


<br>
<br>

## Message



### HelloReply
* **message** (string)  `Required` 

    <br>

### HelloRequest
* **name** (string)  `Required` 

    <br>
