---
description:  
---
# Endpoint

>  **Package : spaceone.api.identity.v1**

## Endpoint

{% hint style="info" %}
**Endpoint Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](endpoint.md#list)|   [EndpointQuery](endpoint.md#endpointquery) |   [EndpointsInfo](endpoint.md#endpointsinfo) | 
 

 
### list
> **POST** /identity/v1/endpoint/list
>


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
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">service</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">endpoint</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ACTIVE</li>
          	<li>INACTIVE</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### EndpointQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| service |string|✘| |
| endpoint_type |string|✘| |
| domain_id |string|✔| |

### EndpointsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of EndpointInfo](endpoint.md#endpointinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
