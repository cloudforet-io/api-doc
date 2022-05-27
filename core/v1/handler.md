---
description:  
---
# Handler

>  **Package : spaceone.api.core.v1**

## 

## Message

### AuthenticationRequest
| Field | Type |  Description |
| :--- | :--- | :--- |
| domain_id |string | |

### AuthenticationResponse
| Field | Type |  Description |
| :--- | :--- | :--- |
| domain_id |string | |
| public_key |string | |

### AuthorizationRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">service</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">resource</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">verb</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">scope</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>SYSTEM</li>
          	<li>DOMAIN</li>
          	<li>PROJECT</li>
          	<li>USER</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">project_group_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">require_project_id</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">require_project_group_id</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">require_user_id</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">require_domain_id</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### AuthorizationResponse
| Field | Type |  Description |
| :--- | :--- | :--- |
| role_type |string | |
| projects |list of string | |
| project_groups |list of string | |

### EventRequest
| Field | Type |  Description |
| :--- | :--- | :--- |
| service |string | |
| resource |string | |
| verb |string | |
| status |string | |
| message |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
