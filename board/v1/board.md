---
description:  
---
# Board

>  **Package : spaceone.api.board.v1**

## Board

{% hint style="info" %}
**Board Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](board.md#create)|   [CreateBoardRequest](board.md#createboardrequest) |   [BoardInfo](board.md#boardinfo) |  |
| [**update**](board.md#update)|   [UpdateBoardRequest](board.md#updateboardrequest) |   [BoardInfo](board.md#boardinfo) |  |
| [**set_categories**](board.md#set_categories)|   [SetBoardCategoriesRequest](board.md#setboardcategoriesrequest) |   [BoardInfo](board.md#boardinfo) |  |
| [**delete**](board.md#delete)|   [BoardRequest](board.md#boardrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](board.md#get)|   [GetBoardRequest](board.md#getboardrequest) |   [BoardInfo](board.md#boardinfo) |  |
| [**list**](board.md#list)|   [BoardQuery](board.md#boardquery) |   [BoardsInfo](board.md#boardsinfo) |  |
| [**stat**](board.md#stat)|   [BoardStatQuery](board.md#boardstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**create**](board.md#create) </div> | <div style="width:200px; text-align:center;">    [CreateBoardRequest](board.md#createboardrequest)  </div> | <div style="width:200px; text-align:center;">   [BoardInfo](board.md#boardinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update**](board.md#update) </div> | <div style="width:200px; text-align:center;">    [UpdateBoardRequest](board.md#updateboardrequest)  </div> | <div style="width:200px; text-align:center;">   [BoardInfo](board.md#boardinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**set_categories**](board.md#set_categories) </div> | <div style="width:200px; text-align:center;">    [SetBoardCategoriesRequest](board.md#setboardcategoriesrequest)  </div> | <div style="width:200px; text-align:center;">   [BoardInfo](board.md#boardinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**delete**](board.md#delete) </div> | <div style="width:200px; text-align:center;">    [BoardRequest](board.md#boardrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](board.md#get) </div> | <div style="width:200px; text-align:center;">    [GetBoardRequest](board.md#getboardrequest)  </div> | <div style="width:200px; text-align:center;">   [BoardInfo](board.md#boardinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](board.md#list) </div> | <div style="width:200px; text-align:center;">    [BoardQuery](board.md#boardquery)  </div> | <div style="width:200px; text-align:center;">   [BoardsInfo](board.md#boardsinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](board.md#stat) </div> | <div style="width:200px; text-align:center;">    [BoardStatQuery](board.md#boardstatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
### create
> **POST** /board/v1/boards
>


| Type | Message |
| :--- | :--- |
| Request | [CreateBoardRequest](board.md#createboardrequest) |
| Response |  [BoardInfo](board.md#boardinfo)  |
 
 

 
### update
> **PUT** /board/v1/board/{board_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateBoardRequest](board.md#updateboardrequest) |
| Response |  [BoardInfo](board.md#boardinfo)  |
 
 

 
### set_categories
> **PUT** /board/v1/board/{board_id}/set-categories
>


| Type | Message |
| :--- | :--- |
| Request | [SetBoardCategoriesRequest](board.md#setboardcategoriesrequest) |
| Response |  [BoardInfo](board.md#boardinfo)  |
 
 

 
### delete
> **DELETE** /board/v1/board/{board_id}
>


| Type | Message |
| :--- | :--- |
| Request | [BoardRequest](board.md#boardrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /board/v1/board/{board_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetBoardRequest](board.md#getboardrequest) |
| Response |  [BoardInfo](board.md#boardinfo)  |
 
 

 
### list
> **GET** /board/v1/boards
>
> **POST** /board/v1/boards/search



| Type | Message |
| :--- | :--- |
| Request | [BoardQuery](board.md#boardquery) |
| Response |  [BoardsInfo](board.md#boardsinfo)  |
 
 

 
### stat
> **POST** /board/v1/boards/stat
>


| Type | Message |
| :--- | :--- |
| Request | [BoardStatQuery](board.md#boardstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### BoardInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| board_id |string | |
| name |string | |
| categories |list of string | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| created_at |string | |

### BoardQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| board_id |string|❌| |
| name |string|❌| |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |

### BoardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| board_id |string|✅| |

### BoardStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |

### BoardsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of BoardInfo](board.md#boardinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateBoardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| categories |list of string|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |

### GetBoardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| board_id |string|✅| |
| only |list of string|❌| |

### SetBoardCategoriesRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| board_id |string|✅| |
| categories |list of string|❌| |

### UpdateBoardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| board_id |string|✅| |
| name |string|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
