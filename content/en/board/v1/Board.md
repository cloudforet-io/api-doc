---
title: "Board"
linkTitle: "Board"
weight: 3
bookFlatSection: true
---
# [Board](#Board)
A Board is a bulletin-board-type resource for posting notices and announcements in Cloudforet.


>  **Package : spaceone.api.board.v1**

<br>
<br>

## Board





**Board Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Board#create) | [CreateBoardRequest](Board#createboardrequest) | [BoardInfo](Board#boardinfo) |
| [**update**](./Board#update) | [UpdateBoardRequest](Board#updateboardrequest) | [BoardInfo](Board#boardinfo) |
| [**set_categories**](./Board#set_categories) | [SetBoardCategoriesRequest](Board#setboardcategoriesrequest) | [BoardInfo](Board#boardinfo) |
| [**delete**](./Board#delete) | [BoardRequest](Board#boardrequest) | [Empty](Board#empty) |
| [**get**](./Board#get) | [BoardRequest](Board#boardrequest) | [BoardInfo](Board#boardinfo) |
| [**list**](./Board#list) | [BoardQuery](Board#boardquery) | [BoardsInfo](Board#boardsinfo) |
| [**stat**](./Board#stat) | [BoardStatQuery](Board#boardstatquery) | [Struct](Board#struct) |



    
<br>

### create

Creates a new Board with SYSTEM permission. The `name` of the board is only required. You can add one or more `categories` representing the Board's attributes.



> **POST** /board/v1/board/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateBoardRequest](./Board#createboardrequest)

* **name** (string)   `Required` 


* **categories** (string)  `Repeated`   


* **tags** (Struct)  





{{< highlight json >}}
{
  "name": "notice",
  "categories": ["admin", "developer", "devops"],
  "tags": {"a": "b"}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[BoardInfo](#BOARDINFO)
* **board_id** (string)   `Required` 

* **name** (string)   `Required` 

* **categories** (string)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
     "board_id": "board-123456789012",
     "name": "notice",
     "categories": [
         "admin",
         "developer",
         "devops"
     ],
     "tags": {
         "a": "b"
     },
     "created_at": "2022-01-01T06:47:27.759Z"
 }
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific Board with SYSTEM permission. You can make changes in Board settings, including `name` and `tags`.



> **POST** /board/v1/board/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateBoardRequest](./Board#updateboardrequest)

* **board_id** (string)   `Required` 


* **name** (string)  


* **tags** (Struct)  





{{< highlight json >}}
{
   "board_id": "board-123456789012",
   "name": "system notice",
   "tags": {"b": "c"}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[BoardInfo](#BOARDINFO)
* **board_id** (string)   `Required` 

* **name** (string)   `Required` 

* **categories** (string)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
     "board_id": "board-123456789012",
     "name": "notice",
     "categories": [
         "admin",
         "developer",
         "devops"
     ],
     "tags": {
         "a": "b"
     },
     "created_at": "2022-01-01T06:47:27.759Z"
 }
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### set_categories

Adds or changes `categories` of a specific Board with SYSTEM permission. A change in `categories` of a Board does not affect the `category` of the child Posts.



> **POST** /board/v1/board/set-categories
>





 {{< tabs " set_categories " >}}

 {{< tab "Request Example" >}}



[SetBoardCategoriesRequest](./Board#setboardcategoriesrequest)

* **board_id** (string)   `Required` 


* **categories** (string)  `Repeated`   





{{< highlight json >}}
{
   "board_id": "board-123456789012",
   "categories": ["Developer", "SRE", "Devops"]
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[BoardInfo](#BOARDINFO)
* **board_id** (string)   `Required` 

* **name** (string)   `Required` 

* **categories** (string)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
     "board_id": "board-123456789012",
     "name": "notice",
     "categories": [
         "admin",
         "developer",
         "devops"
     ],
     "tags": {
         "a": "b"
     },
     "created_at": "2022-01-01T06:47:27.759Z"
 }
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific Board with `SYSTEM` permission. You can delete a Board regardless of the presence of Posts created under the Board.



> **POST** /board/v1/board/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[BoardRequest](./Board#boardrequest)

* **board_id** (string)   `Required` 





{{< highlight json >}}
{
   "board_id": "board-123456789012"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific Board. You must specify the `board_id` of the Board to get. Prints detailed information about the Board, including `name`, `categories`.



> **POST** /board/v1/board/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[BoardRequest](./Board#boardrequest)

* **board_id** (string)   `Required` 





{{< highlight json >}}
{
   "board_id": "board-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[BoardInfo](#BOARDINFO)
* **board_id** (string)   `Required` 

* **name** (string)   `Required` 

* **categories** (string)  `Repeated`   `Required` 

* **tags** (Struct)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
     "board_id": "board-123456789012",
     "name": "notice",
     "categories": [
         "admin",
         "developer",
         "devops"
     ],
     "tags": {
         "a": "b"
     },
     "created_at": "2022-01-01T06:47:27.759Z"
 }
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all Boards. You can use a query to get a filtered list of Boards.



> **POST** /board/v1/board/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[BoardQuery](./Board#boardquery)

* **query** (Query)  


* **board_id** (string)  


* **name** (string)  





{{< highlight json >}}
{
   "query": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[BoardsInfo](#BOARDSINFO)
* **results** (BoardInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
     "results": [
         {
             "board_id": "board-123456789012",
             "name": "dev-notice",
             "categories": [
                 "flower",
                 "school",
                 "spaceone"
             ],
             "tags": {
                 "b": "c"
             },
             "created_at": "2022-01-01T05:16:08.549Z"
         },
         {
             "board_id": "board-987654321098",
             "name": "notice",
             "tags": {
                 "a": "b"
             },
             "created_at": "2022-01-01T05:24:19.758Z"
         }
     ],
     "total_count": 2
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /board/v1/board/stat
>






    


<br>
<br>

## Message



### BoardInfo
* **board_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **categories** (string)  `Repeated`    `Required` 

    
* **tags** (Struct)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### BoardQuery
* **query** (Query)  

    
* **board_id** (string)  

    
* **name** (string)  

    <br>

### BoardRequest
* **board_id** (string)   `Required` 

    <br>

### BoardStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### BoardsInfo
* **results** (BoardInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### CreateBoardRequest
* **name** (string)   `Required` 

    
* **categories** (string)  `Repeated`   

    
* **tags** (Struct)  

    <br>

### SetBoardCategoriesRequest
* **board_id** (string)   `Required` 

    
* **categories** (string)  `Repeated`   

    <br>

### UpdateBoardRequest
* **board_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>
