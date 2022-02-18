---
description:  
---
# Custom widget

>  **Package : spaceone.api.cost_analysis.v1**

## CustomWidget

{% hint style="info" %}
**CustomWidget Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](custom-widget.md#create)|   [CreateCustomWidgetRequest](custom-widget.md#createcustomwidgetrequest) |   [CustomWidgetInfo](custom-widget.md#customwidgetinfo) |  |
| 2 | [**update**](custom-widget.md#update)|   [UpdateCustomWidgetRequest](custom-widget.md#updatecustomwidgetrequest) |   [CustomWidgetInfo](custom-widget.md#customwidgetinfo) |  |
| 3 | [**delete**](custom-widget.md#delete)|   [CustomWidgetRequest](custom-widget.md#customwidgetrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [**get**](custom-widget.md#get)|   [GetCustomWidgetRequest](custom-widget.md#getcustomwidgetrequest) |   [CustomWidgetInfo](custom-widget.md#customwidgetinfo) |  |
| 5 | [**list**](custom-widget.md#list)|   [CustomWidgetQuery](custom-widget.md#customwidgetquery) |   [CustomWidgetsInfo](custom-widget.md#customwidgetsinfo) |  |
| 6 | [**stat**](custom-widget.md#stat)|   [CustomWidgetStatQuery](custom-widget.md#customwidgetstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /cost-analysis/v1/custom-widgets
>


| Type | Message |
| :--- | :--- |
| Request | [CreateCustomWidgetRequest](custom-widget.md#createcustomwidgetrequest) |
| Response |  [CustomWidgetInfo](custom-widget.md#customwidgetinfo)  |
 
 

 
### update
> **PUT** /cost-analysis/v1/custom-widget/{widget_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateCustomWidgetRequest](custom-widget.md#updatecustomwidgetrequest) |
| Response |  [CustomWidgetInfo](custom-widget.md#customwidgetinfo)  |
 
 

 
### delete
> **DELETE** /cost-analysis/v1/custom-widget/{widget_id}
>


| Type | Message |
| :--- | :--- |
| Request | [CustomWidgetRequest](custom-widget.md#customwidgetrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /cost-analysis/v1/custom-widget/{widget_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetCustomWidgetRequest](custom-widget.md#getcustomwidgetrequest) |
| Response |  [CustomWidgetInfo](custom-widget.md#customwidgetinfo)  |
 
 

 
### list
> **GET** /cost-analysis/v1/custom-widgets
>
> **POST** /cost-analysis/v1/custom-widgets/search



| Type | Message |
| :--- | :--- |
| Request | [CustomWidgetQuery](custom-widget.md#customwidgetquery) |
| Response |  [CustomWidgetsInfo](custom-widget.md#customwidgetsinfo)  |
 
 

 
### stat
> **POST** /cost-analysis/v1/custom-widgets/stat
>


| Type | Message |
| :--- | :--- |
| Request | [CustomWidgetStatQuery](custom-widget.md#customwidgetstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateCustomWidgetRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | name |string|✅| |
| 2 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | domain_id |string|✅| |

### CustomWidgetInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | widget_id |string | |
| 2 | name |string | |
| 3 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 5 | user_id |string | |
| 6 | domain_id |string | |
| 7 | created_at |string | |
| 8 | updated_at |string | |

### CustomWidgetQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | widget_id |string|❌| |
| 3 | name |string|❌| |
| 4 | user_id |string|❌| |
| 5 | domain_id |string|✅| |

### CustomWidgetRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | widget_id |string|✅| |
| 2 | domain_id |string|✅| |

### CustomWidgetStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### CustomWidgetsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of CustomWidgetInfo](custom-widget.md#customwidgetinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetCustomWidgetRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | widget_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### UpdateCustomWidgetRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | widget_id |string|✅| |
| 2 | name |string|❌| |
| 3 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 5 | domain_id |string|✅| |
