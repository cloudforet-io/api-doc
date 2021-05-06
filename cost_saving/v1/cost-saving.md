---
description:  
---
# Cost saving

>  **Package : spaceone.api.cost_saving.v1**

## CostSaving

{% hint style="info" %}
**CostSaving Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**record**](cost-saving.md#record)|   [RecordRequest](cost-saving.md#recordrequest) |   [RecordInfo](cost-saving.md#recordinfo) |  |
| 2 | [**list**](cost-saving.md#list)|   [CostSavingQuery](cost-saving.md#costsavingquery) |   [CostSavingsInfo](cost-saving.md#costsavingsinfo) |  |
| 3 | [**stat**](cost-saving.md#stat)|   [CostSavingStatQuery](cost-saving.md#costsavingstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
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
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | cost_saving_id |string | |
| 2 | cost_normal |float | |
| 3 | cost_saving |float | |
| 4 | saving_result |float | |
| 5 | provider |string | |
| 6 | resource_type |string | |
| 7 | region_code |string | |
| 8 | project_id |string | |
| 9 | domain_id |string | |
| 10 | saving_service |string | |
| 11 | saving_by |string | |
| 12 | calc_dimensions |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 13 | saving_begin_at |string | |
| 14 | saving_duration |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
| 15 | created_at |string | |

### CostSavingQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | resource_type |string|❌| |
| 3 | provider |string|❌| |
| 4 | region_code |string|❌| |
| 5 | project_id |string|❌| |
| 6 | saving_service |string|❌| |
| 7 | saving_by |string|❌| |
| 8 | domain_id |string|✅| |

### CostSavingStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### CostSavingsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of CostSavingInfo](cost-saving.md#costsavinginfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### RecordInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">record_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">resource_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">saving_mode</td>
      <td style="text-align:left"><ul>
          	<li>MODE_NONE</li>
          	<li>SAVING</li>
          	<li>NORMAL</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">calc_dimensions</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">region_code</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">saving_service</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">saving_by</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### RecordRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">resource_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">saving_mode</td>
      <td style="text-align:left"><ul>
          	<li>MODE_NONE</li>
          	<li>SAVING</li>
          	<li>NORMAL</li>
        </ul></td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">calc_dimensions</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">saving_service</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">saving_by</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">region_code</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>


