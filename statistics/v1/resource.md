---
description:  
---
# Resource

>  **Package : spaceone.api.statistics.v1**

## Resource

{% hint style="info" %}
**Resource Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :-----: | :--------: | :--------: | :-------------------- |
| [**stat**](resource.md#stat)|   [ResourceStatRequest](resource.md#resourcestatrequest) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

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
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">stat</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ResourceStatRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Struct </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr></tbody>
</table> 
 

 
### stat
> **POST** /statistics/v1/resources/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ResourceStatRequest](resource.md#resourcestatrequest) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### ResourceStatRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| aggregate |[list of StatAggregate](resource.md#stataggregate)|✅| |
| page |[StatPage](resource.md#statpage)|❌| |
| domain_id |string|✅| |

### StatAggregate
| Field | Type |  Description |
| :--- | :--- | :--- |
| query |[StatAggregateQuery](resource.md#stataggregatequery) | |
| join |[StatAggregateJoin](resource.md#stataggregatejoin) | |
| concat |[StatAggregateConcat](resource.md#stataggregateconcat) | |
| sort |[StatAggregateSort](resource.md#stataggregatesort) | |
| formula |[StatAggregateFormula](resource.md#stataggregateformula) | |
| fill_na |[StatAggregateFillNA](resource.md#stataggregatefillna) | |

### StatAggregateConcat
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| resource_type |string|✅| |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| extend_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |

### StatAggregateFillNA
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### StatAggregateFormula
| Field | Type |  Description |
| :--- | :--- | :--- |
| eval |string | |
| query |string | |

### StatAggregateJoin
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
      <td style="text-align:left; width:100px;">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query">spaceone.api.core.v1.StatisticsQuery</a></td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">extend_data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">type</td>
      <td style="text-align:left"><ul>
          	<li>LEFT</li>
          	<li>RIGHT</li>
          	<li>OUTER</li>
          	<li>INNER</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">keys</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### StatAggregateQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| resource_type |string|✅| |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| extend_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |

### StatAggregateSort
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| key |string|✅| |
| desc |bool|❌| |

### StatPage
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| start |[uint32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|❌| |
| limit |[uint32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✅| |
