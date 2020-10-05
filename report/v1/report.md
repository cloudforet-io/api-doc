---
description:  
---
# Report

>  **Package : spaceone.api.report.v1**

## Report

{% hint style="info" %}
**Report Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**get**](report.md#get)|   [GetReportRequest](report.md#getreportrequest) |   [ReportInfo](report.md#reportinfo) |  |
| 2 | [**get_download_url**](report.md#get_download_url)|   [GetDownloadURLRequest](report.md#getdownloadurlrequest) |   [ReportDownloadInfo](report.md#reportdownloadinfo) |  |
| 3 | [**list**](report.md#list)|   [ReportQuery](report.md#reportquery) |   [ReportsInfo](report.md#reportsinfo) |  |
| 4 | [**create**](report.md#create)|   [CreateReportRequest](report.md#createreportrequest) |   [ReportInfo](report.md#reportinfo) |  | 
 

 
### get
> **GET** /report/v1/report/{report_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetReportRequest](report.md#getreportrequest) |
| Response |  [ReportInfo](report.md#reportinfo)  |
 
 

 
### get_download_url
> **GET** /report/v1/report/{report_id}/download_url
>


| Type | Message |
| :--- | :--- |
| Request | [GetDownloadURLRequest](report.md#getdownloadurlrequest) |
| Response |  [ReportDownloadInfo](report.md#reportdownloadinfo)  |
 
 

 
### list
> **GET** /report/v1/reports
>
> **POST** /report/v1/reports/search



| Type | Message |
| :--- | :--- |
| Request | [ReportQuery](report.md#reportquery) |
| Response |  [ReportsInfo](report.md#reportsinfo)  |
 
 

 
### create
> **POST** /report/v1/reports
>


| Type | Message |
| :--- | :--- |
| Request | [CreateReportRequest](report.md#createreportrequest) |
| Response |  [ReportInfo](report.md#reportinfo)  |


## 

## Message

### CreateReportRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | template_id |string|✅| |
| 3 | name |string|✅| |
| 4 | template_options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 5 | storage_id |string|❌| |

### GetDownloadURLRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | report_id |string|✅| |

### GetReportRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string|✅| |
| 2 | report_id |string|✅| |
| 3 | only |list of string|❌| |

### ReportDownloadInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | download_url |string | |

### ReportError
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | code |string | |
| 2 | message |string | |

### ReportInfo
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
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">report_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">template_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">storage_info</td>
      <td style="text-align:left"><a href="report.md#storageinfo">StorageInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">storage_path</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">template_options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>CREATED</li>
          	<li>IN_PROGRESS</li>
          	<li>FAILURE</li>
          	<li>TIMEOUT</li>
          	<li>CANCELED</li>
          	<li>FINISHED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">created_by</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">schedule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">error</td>
      <td style="text-align:left"><a href="report.md#reporterror">ReportError</a></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### ReportQuery
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
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">report_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">template_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">storage_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">schedule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">created_by</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>CREATED</li>
          	<li>IN_PROGRESS</li>
          	<li>FAILURE</li>
          	<li>TIMEOUT</li>
          	<li>CANCELED</li>
          	<li>FINISHED</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### ReportsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of ReportInfo](report.md#reportinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
