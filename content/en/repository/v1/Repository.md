---
title: "Repository"
linkTitle: "Repository"
weight: 3
bookFlatSection: true
---
# [Repository](#Repository)
A Repository is a repository storing data of deployable plugins.


>  **Package : spaceone.api.repository.v1**

<br>
<br>

## Repository





**Repository Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](./Repository#list) | [RepositoryQuery](Repository#repositoryquery) | [RepositoriesInfo](Repository#repositoriesinfo) |



    
<br>

### list

Gets a list of all Repositories regardless of `domain`. You can use a query to get a filtered list of Repositories.



> **POST** /repository/v1/repository/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[RepositoryQuery](./Repository#repositoryquery)

* **repository_id** (string)  


* **repository_type** (string)  





{{< highlight json >}}
{
   "query": {},
   "repository_id": "repo-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[RepositoriesInfo](#REPOSITORIESINFO)
* **results** (RepositoryInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
   "results": [
       {
           "repository_id": "repo-123456789012",
           "name": "Open Source Marketplace",
           "repository_type": "remote",
           "endpoint": "grpc+ssl://repository.portal.spaceone.megazone.io:443",
       }
   ],
   "total_count": 1
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    


<br>
<br>

## Message



### RepositoriesInfo
* **results** (RepositoryInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### RepositoryInfo
* **repository_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **repository_type** (string)   `Required` 

    
* **endpoint** (string)   `Required` 

    <br>

### RepositoryQuery
* **repository_id** (string)  

    
* **repository_type** (string)  

    <br>
