---
title: "Board"
linkTitle: "Board"
weight: 3
bookFlatSection: true
---
# [Board](#Board)
desc: A Board is a bulletin-board-type resource for posting notices and announcements in Cloudforet.


>  **Package : spaceone.api.board.v1**

<br>
<br>

## Board


**Board Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Board#create) | [CreateBoardRequest](Board#createboardrequest) | [BoardInfo](./Board#boardinfo) |
| [**update**](./Board#update) | [UpdateBoardRequest](Board#updateboardrequest) | [BoardInfo](./Board#boardinfo) |
| [**set_categories**](./Board#set_categories) | [SetBoardCategoriesRequest](Board#setboardcategoriesrequest) | [BoardInfo](./Board#boardinfo) |
| [**delete**](./Board#delete) | [BoardRequest](Board#boardrequest) | [Empty](./Board#empty) |
| [**get**](./Board#get) | [GetBoardRequest](Board#getboardrequest) | [BoardInfo](./Board#boardinfo) |
| [**list**](./Board#list) | [BoardQuery](Board#boardquery) | [BoardsInfo](./Board#boardsinfo) |
| [**stat**](./Board#stat) | [BoardStatQuery](Board#boardstatquery) | [Struct](./Board#struct) |



    
<br>

### create

> **POST** /board/v1/board/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /board/v1/board/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### set_categories

> **POST** /board/v1/board/set-categories
>




 {{< tabs " set_categories " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /board/v1/board/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /board/v1/board/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /board/v1/board/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /board/v1/board/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### BoardInfo
* **board_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **categories** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### BoardQuery
* **board_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **query** (Query)  `Required` 

  *is_required: false*

    <br>

### BoardRequest
* **board_id** (string)  `Required` 

  *is_required: true*

    <br>

### BoardStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    <br>

### BoardsInfo
* **results** (BoardInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### CreateBoardRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **categories** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    <br>

### GetBoardRequest
* **board_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### SetBoardCategoriesRequest
* **board_id** (string)  `Required` 

  *is_required: true*

    
* **categories** (string)  `Required` 

  *is_required: false*

    <br>

### UpdateBoardRequest
* **board_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    <br>
