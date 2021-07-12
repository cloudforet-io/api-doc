---
description:  
---
# Endpoint

>  **Package : spaceone.api.identity.v1**

## Endpoint

{% hint style="info" %}
**Endpoint Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**list**](endpoint.md#list)|   [EndpointQuery](endpoint.md#endpointquery) |   [EndpointsInfo](endpoint.md#endpointsinfo) |  | 
 

 
### list
> **GET** /identity/v1/endpoints
>
> **POST** /identity/v1/endpoints/search



| Type | Message |
| :--- | :--- |
| Request | [EndpointQuery](endpoint.md#endpointquery) |
| Response |  [EndpointsInfo](endpoint.md#endpointsinfo)  |


## 

## Message

### EndpointInfo
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
      <td style="text-align:left">service</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">endpoint</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ACTIVE</li>
          	<li>INACTIVE</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### EndpointQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | service |string|❌| |
| 3 | domain_id |string|✅| |

### EndpointsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of EndpointInfo](endpoint.md#endpointinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
