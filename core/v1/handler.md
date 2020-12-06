---
description:  
---
# Handler

>  **Package : spaceone.api.core.v1**

## 

## Message

### AuthenticationRequest
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | domain_id |string | |

### AuthenticationResponse
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | domain_id |string | |
| 2 | public_key |string | |

### AuthorizationRequest
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
      <td style="text-align:left">resource</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">verb</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">scope</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>PROJECT</li>
          	<li>SYSTEM</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">project_group_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### AuthorizationResponse
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | role_type |string | |

### EventRequest
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | service |string | |
| 2 | resource |string | |
| 3 | verb |string | |
| 4 | status |string | |
| 5 | message |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
