---
description: A UserDashboard is a cost data dashboard customized with a combination of widgets a User want.
---
# User dashboard

>  **Package : spaceone.api.cost_analysis.v1**

## UserDashboard

{% hint style="info" %}
**UserDashboard Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](user-dashboard.md#create)|   [CreateUserDashboardRequest](user-dashboard.md#createuserdashboardrequest) |   [UserDashboardInfo](user-dashboard.md#userdashboardinfo) |
| [**update**](user-dashboard.md#update)|   [UpdateUserDashboardRequest](user-dashboard.md#updateuserdashboardrequest) |   [UserDashboardInfo](user-dashboard.md#userdashboardinfo) |
| [**delete**](user-dashboard.md#delete)|   [UserDashboardRequest](user-dashboard.md#userdashboardrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](user-dashboard.md#get)|   [GetUserDashboardRequest](user-dashboard.md#getuserdashboardrequest) |   [UserDashboardInfo](user-dashboard.md#userdashboardinfo) |
| [**list**](user-dashboard.md#list)|   [UserDashboardQuery](user-dashboard.md#userdashboardquery) |   [UserDashboardsInfo](user-dashboard.md#userdashboardsinfo) |
| [**stat**](user-dashboard.md#stat)|   [UserDashboardStatQuery](user-dashboard.md#userdashboardstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** cost-analysis/v1/user-dashboard/create
>

> Creates a new UserDashboard. Users can use the dashboard in `private`. In addition to the widgets provided by Cloudforet by default, Users can use widgets through the CustomWidget resource to create a UserDashboard that suits their needs.

| Type | Message |
| :--- | :--- |
| Request | [CreateUserDashboardRequest](user-dashboard.md#createuserdashboardrequest) |
| Response |  [UserDashboardInfo](user-dashboard.md#userdashboardinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "Untitled Dashboard",
    "custom_layouts": [
        [
            {
                "name": "AWS Data-Transfer Cost Trend",
                "widget_id": "linegraph-lg-02",
                "options": {
                    "layout": 100.0,
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_COST_TREND_DESC",
                    "chart_type": "LINE",
                    "chart_img": "AWS_Data-Transfer_Cost_Trend"
                }
            }
        ],
        [
            {
                "options": {
                    "chart_type": "MAP",
                    "chart_img": "AWS_Data-Transfer_By_Region",
                    "layout": 100.0,
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_BY_REGION_DESC"
                },
                "name": "AWS Data-Transfer by Region",
                "widget_id": "map-lg-02"
            }
        ],
        [
            {
                "options": {
                    "group_by": "project_id",
                    "layout": 100.0,
                    "chart_type": "STACKED_COLUMN",
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_CLOUDFRONT_COST_DESC",
                    "chart_img": "AWS_CloudFront_Cost"
                },
                "name": "AWS CloudFront Cost by Project",
                "widget_id": "stackedcol-lg-03"
            }
        ]
    ],
    "default_filter": {},
    "period_type": "AUTO"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "user_dashboard_id": "user-dash-bf3f5f5ffa03",
    "name": "Untitled Dashboard",
    "custom_layouts": [
        [
            {
                "options": {
                    "chart_type": "LINE",
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_COST_TREND_DESC",
                    "layout": 100.0,
                    "chart_img": "AWS_Data-Transfer_Cost_Trend"
                },
                "widget_id": "linegraph-lg-02",
                "name": "AWS Data-Transfer Cost Trend"
            }
        ],
        [
            {
                "name": "AWS Data-Transfer by Region",
                "widget_id": "map-lg-02",
                "options": {
                    "chart_img": "AWS_Data-Transfer_By_Region",
                    "chart_type": "MAP",
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_BY_REGION_DESC",
                    "layout": 100.0
                }
            }
        ],
        [
            {
                "widget_id": "stackedcol-lg-03",
                "name": "AWS CloudFront Cost by Project",
                "options": {
                    "layout": 100.0,
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_CLOUDFRONT_COST_DESC",
                    "chart_img": "AWS_CloudFront_Cost",
                    "group_by": "project_id",
                    "chart_type": "STACKED_COLUMN"
                }
            }
        ]
    ],
    "default_filter": {},
    "period_type": "AUTO",
    "tags": {},
    "user_id": "seolmin@mz.co.kr",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-19T05:58:52.065Z",
    "updated_at": "2022-07-19T05:58:52.065Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **POST** cost-analysis/v1/user-dashboard/update
>

> Updates a specific UserDashboard. You can make changes in widgets, including default widgets and CustomWidegets.

| Type | Message |
| :--- | :--- |
| Request | [UpdateUserDashboardRequest](user-dashboard.md#updateuserdashboardrequest) |
| Response |  [UserDashboardInfo](user-dashboard.md#userdashboardinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "user_dashboard_id": "user-dash-bf3f5f5ffa03",
    "name": "Untitled Dashboard2",
    "custom_layouts": [
        [
            {
                "options": {
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_COST_TREND_DESC",
                    "chart_type": "LINE",
                    "chart_img": "AWS_Data-Transfer_Cost_Trend",
                    "layout": 100.0
                },
                "name": "AWS Data-Transfer Cost Trend",
                "widget_id": "linegraph-lg-02"
            }
        ],
        [
            {
                "name": "AWS Data-Transfer by Region",
                "options": {
                    "chart_type": "MAP",
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_BY_REGION_DESC",
                    "layout": 100.0,
                    "chart_img": "AWS_Data-Transfer_By_Region"
                },
                "widget_id": "map-lg-02"
            }
        ],
        [
            {
                "name": "AWS CloudFront Cost by Project",
                "widget_id": "stackedcol-lg-03",
                "options": {
                    "layout": 100.0,
                    "chart_img": "AWS_CloudFront_Cost",
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_CLOUDFRONT_COST_DESC",
                    "chart_type": "STACKED_COLUMN",
                    "group_by": "project_id"
                }
            }
        ]
    ]
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "user_dashboard_id": "user-dash-bf3f5f5ffa03",
    "name": "Untitled Dashboard2",
    "custom_layouts": [
        [
            {
                "options": {
                    "chart_type": "LINE",
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_COST_TREND_DESC",
                    "layout": 100.0,
                    "chart_img": "AWS_Data-Transfer_Cost_Trend"
                },
                "widget_id": "linegraph-lg-02",
                "name": "AWS Data-Transfer Cost Trend"
            }
        ],
        [
            {
                "name": "AWS Data-Transfer by Region",
                "widget_id": "map-lg-02",
                "options": {
                    "chart_img": "AWS_Data-Transfer_By_Region",
                    "chart_type": "MAP",
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_BY_REGION_DESC",
                    "layout": 100.0
                }
            }
        ],
        [
            {
                "widget_id": "stackedcol-lg-03",
                "name": "AWS CloudFront Cost by Project",
                "options": {
                    "layout": 100.0,
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_CLOUDFRONT_COST_DESC",
                    "chart_img": "AWS_CloudFront_Cost",
                    "group_by": "project_id",
                    "chart_type": "STACKED_COLUMN"
                }
            }
        ]
    ],
    "default_filter": {},
    "period_type": "AUTO",
    "tags": {},
    "user_id": "seolmin@mz.co.kr",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-19T05:58:52.065Z",
    "updated_at": "2022-07-19T05:58:52.065Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **POST** cost-analysis/v1/user-dashboard/delete
>

> Deletes a specific UserDashboard. You must specify the `user_dashboard_id` of the UserDashboard to delete.

| Type | Message |
| :--- | :--- |
| Request | [UserDashboardRequest](user-dashboard.md#userdashboardrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "user_dashboard_id": "user-dash-d1bd5d8cb6d7"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **POST** cost-analysis/v1/user-dashboard/get
>

> Gets a specific UserDashboard. Prints detailed information about the UserDashboard, including widegts used.

| Type | Message |
| :--- | :--- |
| Request | [GetUserDashboardRequest](user-dashboard.md#getuserdashboardrequest) |
| Response |  [UserDashboardInfo](user-dashboard.md#userdashboardinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "user_dashboard_id": "user-dash-d1bd5d8cb6d7"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "user_dashboard_id": "user-dash-d1bd5d8cb6d7",
    "name": "11 Months Public Cloud Cost Summary",
    "custom_layouts": [
        [
            {
                "widget_id": "card-lg-01",
                "options": {
                    "chart_type": "CARD",
                    "layout": 100.0
                },
                "name": "Budget Usage Summary"
            }
        ],
        [
            {
                "options": {
                    "layout": 100.0,
                    "chart_type": "TABLE"
                },
                "name": "Project-wise Budget Usage Summary@@",
                "widget_id": "table-lg-01"
            }
        ],
        [
            {
                "name": "Cost Trend By Product",
                "options": {
                    "chart_type": "STACKED_COLUMN",
                    "layout": 100.0,
                    "group_by": "product"
                },
                "widget_id": "stackedcol-lg-02"
            }
        ]
    ],
    "default_filter": {
        "project_id": []
    },
    "period_type": "FIXED",
    "period": {
        "start": "2021-04-01",
        "end": "2022-02-28"
    },
    "tags": {},
    "user_id": "wanzargen@mz.co.kr",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-03-03T03:36:35.396Z",
    "updated_at": "2022-03-03T03:36:35.396Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **POST** cost-analysis/v1/user-dashboard/list
>

> Gets a list of all UserDashboards. You can use a query to get a filtered list of UserDashboards.

| Type | Message |
| :--- | :--- |
| Request | [UserDashboardQuery](user-dashboard.md#userdashboardquery) |
| Response |  [UserDashboardsInfo](user-dashboard.md#userdashboardsinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {}
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "user_dashboard_id": "user-dash-d1bd5d8cb6d7",
            "name": "11 Months Public Cloud Cost Summary",
            "custom_layouts": [
                [
                    {
                        "options": {
                            "layout": 100.0,
                            "chart_type": "CARD"
                        },
                        "widget_id": "card-lg-01",
                        "name": "Budget Usage Summary"
                    }
                ],
                [
                    {
                        "name": "Project-wise Budget Usage Summary@@",
                        "options": {
                            "chart_type": "TABLE",
                            "layout": 100.0
                        },
                        "widget_id": "table-lg-01"
                    }
                ],
                [
                    {
                        "widget_id": "stackedcol-lg-02",
                        "options": {
                            "layout": 100.0,
                            "group_by": "product",
                            "chart_type": "STACKED_COLUMN"
                        },
                        "name": "Cost Trend By Product"
                    }
                ]
            ],
            "default_filter": {
                "project_id": []
            },
            "period_type": "FIXED",
            "period": {
                "start": "2021-04-01",
                "end": "2022-02-28"
            },
            "tags": {},
            "user_id": "wanzargen@mz.co.kr",
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-03-03T03:36:35.396Z",
            "updated_at": "2022-03-03T03:36:35.396Z"
        },
        {
            "user_dashboard_id": "user-dash-965b03793d5b",
            "name": "AWS CloudFront Cost by Project",
            "custom_layouts": [
                [
                    {
                        "name": "AWS CloudFront Cost by Project",
                        "widget_id": "stackedcol-lg-03",
                        "options": {
                            "chart_type": "STACKED_COLUMN",
                            "layout": 100.0
                        }
                    }
                ],
                [
                    {
                        "widget_id": "stackedcol-lg-03",
                        "options": {
                            "layout": 100.0,
                            "chart_type": "STACKED_COLUMN",
                            "group_by": "service_account_id"
                        },
                        "name": "AWS CloudFront Cost by Service Account"
                    }
                ],
                [
                    {
                        "options": {
                            "layout": 100.0,
                            "chart_type": "LINE"
                        },
                        "name": "AWS Data-Transfer Cost Trend",
                        "widget_id": "linegraph-lg-02"
                    }
                ]
            ],
            "default_filter": {},
            "period_type": "FIXED",
            "period": {
                "start": "2021-05-01",
                "end": "2022-04-30"
            },
            "tags": {},
            "user_id": "wanzargen@mz.co.kr",
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-04-07T01:13:28.494Z",
            "updated_at": "2022-04-07T01:13:28.494Z"
        }
    ],
    "total_count": 48
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** cost-analysis/v1/user-dashboard/stat
>


| Type | Message |
| :--- | :--- |
| Request | [UserDashboardStatQuery](user-dashboard.md#userdashboardstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateUserDashboardRequest
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
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">default_layout_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">custom_layouts</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">default_filter</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">period_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>AUTO</li>
          	<li>FIXED</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">period</td>
      <td style="text-align:left"><a href="user-dashboard.md#userdashboardperiod">UserDashboardPeriod</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### GetUserDashboardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| user_dashboard_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### UpdateUserDashboardRequest
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
      <td style="text-align:left; width:100px;">user_dashboard_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">default_layout_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">custom_layouts</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">default_filter</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">period_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>AUTO</li>
          	<li>FIXED</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">period</td>
      <td style="text-align:left"><a href="user-dashboard.md#userdashboardperiod">UserDashboardPeriod</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### UserDashboardInfo
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
      <td style="text-align:left; width:100px;">user_dashboard_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">default_layout_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">custom_layouts</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">default_filter</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">period_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>AUTO</li>
          	<li>FIXED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">period</td>
      <td style="text-align:left"><a href="user-dashboard.md#userdashboardperiod">UserDashboardPeriod</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">updated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### UserDashboardPeriod
| Field | Type |  Description |
| :--- | :--- | :--- |
| start |string | |
| end |string | |

### UserDashboardQuery
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
      <td style="text-align:left; width:100px;">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">user_dashboard_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">period_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>AUTO</li>
          	<li>FIXED</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### UserDashboardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| user_dashboard_id |string|✔| |
| domain_id |string|✔| |

### UserDashboardStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### UserDashboardsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of UserDashboardInfo](user-dashboard.md#userdashboardinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
