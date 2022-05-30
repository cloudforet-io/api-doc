---
description:  
---
# Custom widget

>  **Package : spaceone.api.cost_analysis.v1**

## CustomWidget

{% hint style="info" %}
**CustomWidget Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](custom-widget.md#create)|   [CreateCustomWidgetRequest](custom-widget.md#createcustomwidgetrequest) |   [CustomWidgetInfo](custom-widget.md#customwidgetinfo) |  |
| [**update**](custom-widget.md#update)|   [UpdateCustomWidgetRequest](custom-widget.md#updatecustomwidgetrequest) |   [CustomWidgetInfo](custom-widget.md#customwidgetinfo) |  |
| [**delete**](custom-widget.md#delete)|   [CustomWidgetRequest](custom-widget.md#customwidgetrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](custom-widget.md#get)|   [GetCustomWidgetRequest](custom-widget.md#getcustomwidgetrequest) |   [CustomWidgetInfo](custom-widget.md#customwidgetinfo) |  |
| [**list**](custom-widget.md#list)|   [CustomWidgetQuery](custom-widget.md#customwidgetquery) |   [CustomWidgetsInfo](custom-widget.md#customwidgetsinfo) |  |
| [**stat**](custom-widget.md#stat)|   [CustomWidgetStatQuery](custom-widget.md#customwidgetstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

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
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CreateCustomWidgetRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CustomWidgetInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">update</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   UpdateCustomWidgetRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CustomWidgetInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">delete</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CustomWidgetRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Empty </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">get</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   GetCustomWidgetRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CustomWidgetInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">list</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CustomWidgetQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CustomWidgetsInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">stat</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CustomWidgetStatQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Struct </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr></tbody>
</table> 
 

 
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
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |

### CustomWidgetInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| widget_id |string | |
| name |string | |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| user_id |string | |
| domain_id |string | |
| created_at |string | |
| updated_at |string | |

### CustomWidgetQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| widget_id |string|❌| |
| name |string|❌| |
| user_id |string|❌| |
| domain_id |string|✅| |

### CustomWidgetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| widget_id |string|✅| |
| domain_id |string|✅| |

### CustomWidgetStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### CustomWidgetsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of CustomWidgetInfo](custom-widget.md#customwidgetinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetCustomWidgetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| widget_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### UpdateCustomWidgetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| widget_id |string|✅| |
| name |string|❌| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |
