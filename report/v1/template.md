---
description:  
---
# Template

>  **Package : spaceone.api.report.v1**

## Template

{% hint style="info" %}
**Template Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**get**](template.md#get)|   [GetTemplateRequest](template.md#gettemplaterequest) |   [TemplateInfo](template.md#templateinfo) |  |
| 2 | [**list**](template.md#list)|   [TemplateQuery](template.md#templatequery) |   [TemplatesInfo](template.md#templatesinfo) |  | 
 

 
### get
> **POST** /report/v1/template/{template_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetTemplateRequest](template.md#gettemplaterequest) |
| Response |  [TemplateInfo](template.md#templateinfo)  |
 
 

 
### list
> **GET** /report/v1/templates
>
> **POST** /report/v1/templates/search



| Type | Message |
| :--- | :--- |
| Request | [TemplateQuery](template.md#templatequery) |
| Response |  [TemplatesInfo](template.md#templatesinfo)  |


## 

## Message

### GetTemplateRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | template_id |string|✅| |
| 3 | only |string|❌| |

### TemplateInfo
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
      <td style="text-align:left">template_id</td>
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
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>ENABLE</li>
          	<li>DISABLE</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### TemplateQuery
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
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">template_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>ENABLE</li>
          	<li>DISABLE</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### TemplatesInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[TemplateInfo](template.md#templateinfo)| |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)| |
