---
description:  
---
# Cost saving

>  **Package : spaceone.api.cost_saving.v1**

## CostSaving

{% hint style="info" %}
**CostSaving Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**record**](cost-saving.md#record)|   [RecordRequest](cost-saving.md#recordrequest) |   [RecordInfo](cost-saving.md#recordinfo) |
| [**list**](cost-saving.md#list)|   [CostSavingQuery](cost-saving.md#costsavingquery) |   [CostSavingsInfo](cost-saving.md#costsavingsinfo) |
| [**stat**](cost-saving.md#stat)|   [CostSavingStatQuery](cost-saving.md#costsavingstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### record
> **POST** /cost-saving/v1/record
>


| Type | Message |
| :--- | :--- |
| Request | [RecordRequest](cost-saving.md#recordrequest) |
| Response |  [RecordInfo](cost-saving.md#recordinfo)  |
 
 

 
### list
> **GET** /cost-saving/v1/cost-savings
>
> **POST** /cost-saving/v1/cost-savings/search



| Type | Message |
| :--- | :--- |
| Request | [CostSavingQuery](cost-saving.md#costsavingquery) |
| Response |  [CostSavingsInfo](cost-saving.md#costsavingsinfo)  |
 
 

 
### stat
> **POST** /cost-saving/v1/cost-savings/stat
>


| Type | Message |
| :--- | :--- |
| Request | [CostSavingStatQuery](cost-saving.md#costsavingstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CostSavingInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| cost_saving_id |string | |
| cost_normal |float | |
| cost_saving |float | |
| saving_result |float | |
| provider |string | |
| resource_type |string | |
| region_code |string | |
| project_id |string | |
| domain_id |string | |
| saving_service |string | |
| saving_by |string | |
| calc_dimensions |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| saving_begin_at |string | |
| saving_duration |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
| created_at |string | |

### CostSavingQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| resource_type |string|❌| |
| provider |string|❌| |
| region_code |string|❌| |
| project_id |string|❌| |
| saving_service |string|❌| |
| saving_by |string|❌| |
| domain_id |string|✅| |

### CostSavingStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### CostSavingsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of CostSavingInfo](cost-saving.md#costsavinginfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### RecordInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">record_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">resource_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">saving_mode</td>
      <td style="text-align:left"><ul>
          	<li>MODE_NONE</li>
          	<li>SAVING</li>
          	<li>NORMAL</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">calc_dimensions</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">region_code</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">saving_service</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">saving_by</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### RecordRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">resource_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">saving_mode</td>
      <td style="text-align:left"><ul>
          	<li>MODE_NONE</li>
          	<li>SAVING</li>
          	<li>NORMAL</li>
        </ul></td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">calc_dimensions</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">saving_service</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">saving_by</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">region_code</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>


