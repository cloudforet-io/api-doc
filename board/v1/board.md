---
description:  
---
# Board

>  **Package : spaceone.api.board.v1**

## Board

{% hint style="info" %}
**Board Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](board.md#create)|   [CreateBoardRequest](board.md#createboardrequest) |   [BoardInfo](board.md#boardinfo) |  |
| 2 | [**update**](board.md#update)|   [UpdateBoardRequest](board.md#updateboardrequest) |   [BoardInfo](board.md#boardinfo) |  |
| 3 | [**set_categories**](board.md#set_categories)|   [SetBoardCategoriesRequest](board.md#setboardcategoriesrequest) |   [BoardInfo](board.md#boardinfo) |  |
| 4 | [**delete**](board.md#delete)|   [BoardRequest](board.md#boardrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [**get**](board.md#get)|   [GetBoardRequest](board.md#getboardrequest) |   [BoardInfo](board.md#boardinfo) |  |
| 6 | [**list**](board.md#list)|   [BoardQuery](board.md#boardquery) |   [BoardsInfo](board.md#boardsinfo) |  |
| 7 | [**stat**](board.md#stat)|   [BoardStatQuery](board.md#boardstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
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
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | board_id |string | |
| 2 | name |string | |
| 3 | categories |list of string | |
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 5 | created_at |string | |

### BoardQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | board_id |string|❌| |
| 2 | name |string|❌| |
| 3 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |

### BoardRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | board_id |string|✅| |

### BoardStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |

### BoardsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of BoardInfo](board.md#boardinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateBoardRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | name |string|✅| |
| 2 | categories |list of string|❌| |
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |

### GetBoardRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | board_id |string|✅| |
| 2 | only |list of string|❌| |

### SetBoardCategoriesRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | board_id |string|✅| |
| 2 | categories |list of string|❌| |

### UpdateBoardRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | board_id |string|✅| |
| 2 | name |string|❌| |
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
