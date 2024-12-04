---
title: "Comment"
linkTitle: "Comment"
weight: 3
bookFlatSection: true
---
# [Comment](#Comment)



>  **Package : spaceone.api.opsflow.v1**

<br>
<br>

## Comment





**Comment Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Comment#create) | [CommentCreateRequest](Comment#commentcreaterequest) | [CommentInfo](Comment#commentinfo) |
| [**update**](./Comment#update) | [CommentUpdateRequest](Comment#commentupdaterequest) | [CommentInfo](Comment#commentinfo) |
| [**delete**](./Comment#delete) | [CommentRequest](Comment#commentrequest) | [Empty](Comment#empty) |
| [**get**](./Comment#get) | [CommentRequest](Comment#commentrequest) | [CommentInfo](Comment#commentinfo) |
| [**list**](./Comment#list) | [CommentSearchQuery](Comment#commentsearchquery) | [CommentsInfo](Comment#commentsinfo) |
| [**stat**](./Comment#stat) | [CommentStatQuery](Comment#commentstatquery) | [Struct](Comment#struct) |



    
<br>

### create





> **POST** /opsflow/v1/comment/create
>






    
<br>

### update





> **POST** /opsflow/v1/comment/update
>






    
<br>

### delete





> **POST** /opsflow/v1/comment/delete
>






    
<br>

### get





> **POST** /opsflow/v1/comment/get
>






    
<br>

### list





> **POST** /opsflow/v1/comment/list
>






    
<br>

### stat





> **POST** /opsflow/v1/comment/stat
>






    


<br>
<br>

## Message



### CommentCreateRequest
* **task_id** (string)   `Required` 

    
* **comment** (string)   `Required` 

    
* **mentions** (Mentions)  

    <br>

### CommentInfo
* **comment_id** (string)   `Required` 

    
* **comment** (string)   `Required` 

    
* **comment_type** (CommentType)   `Required` 

    
* **is_edited** (bool)   `Required` 

    
* **mentions** (Mentions)   `Required` 

    
* **created_by** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **task_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### CommentRequest
* **comment_id** (string)   `Required` 

    <br>

### CommentSearchQuery
* **query** (Query)  

    
* **task_id** (string)  

    
* **comment_id** (string)  

    
* **comment_type** (CommentType)  

    
* **user_id** (string)  

    
* **user_group_id** (string)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    <br>

### CommentStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### CommentUpdateRequest
* **comment_id** (string)   `Required` 

    
* **comment** (string)   `Required` 

    
* **mentions** (Mentions)  

    <br>

### CommentsInfo
* **results** (CommentInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### Mentions
* **USER** (string)  `Repeated`    `Required` 

    
* **USER_GROUP** (string)  `Repeated`    `Required` 

    <br>
