---
description:  
---
# Board

>  **Package : spaceone.api.board.v1**

## Board

{% hint style="info" %}
**Board Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](board.md#create)|   [CreateBoardRequest](board.md#createboardrequest) |   [BoardInfo](board.md#boardinfo) |  |
| [**update**](board.md#update)|   [UpdateBoardRequest](board.md#updateboardrequest) |   [BoardInfo](board.md#boardinfo) |  |
| [**set_categories**](board.md#set_categories)|   [SetBoardCategoriesRequest](board.md#setboardcategoriesrequest) |   [BoardInfo](board.md#boardinfo) |  |
| [**delete**](board.md#delete)|   [BoardRequest](board.md#boardrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](board.md#get)|   [GetBoardRequest](board.md#getboardrequest) |   [BoardInfo](board.md#boardinfo) |  |
| [**list**](board.md#list)|   [BoardQuery](board.md#boardquery) |   [BoardsInfo](board.md#boardsinfo) |  |
| [**stat**](board.md#stat)|   [BoardStatQuery](board.md#boardstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

<table style="border-collapse: collapse; text-align: left; line-height: 1.5;">
    <thead>
    <tr>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Method</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Request</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Response</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">create</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CreateBoardRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   BoardInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">update</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   UpdateBoardRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   BoardInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">set_categories</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   SetBoardCategoriesRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   BoardInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">delete</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   BoardRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Empty </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">get</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   GetBoardRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   BoardInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">list</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   BoardQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   BoardsInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">stat</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   BoardStatQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Struct </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr></tbody>
</table> 
 

 
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
