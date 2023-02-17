---
description: A PublicDashboard is a cost data dashboard provided to all users by default.
---
# Public dashboard

>  **Package : spaceone.api.cost_analysis.v1**

## PublicDashboard

{% hint style="info" %}
**PublicDashboard Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](public-dashboard.md#create)|   [CreatePublicDashboardRequest](public-dashboard.md#createpublicdashboardrequest) |   [PublicDashboardInfo](public-dashboard.md#publicdashboardinfo) |
| [**update**](public-dashboard.md#update)|   [UpdatePublicDashboardRequest](public-dashboard.md#updatepublicdashboardrequest) |   [PublicDashboardInfo](public-dashboard.md#publicdashboardinfo) |
| [**delete**](public-dashboard.md#delete)|   [PublicDashboardRequest](public-dashboard.md#publicdashboardrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](public-dashboard.md#get)|   [GetPublicDashboardRequest](public-dashboard.md#getpublicdashboardrequest) |   [PublicDashboardInfo](public-dashboard.md#publicdashboardinfo) |
| [**list**](public-dashboard.md#list)|   [PublicDashboardQuery](public-dashboard.md#publicdashboardquery) |   [PublicDashboardsInfo](public-dashboard.md#publicdashboardsinfo) |
| [**stat**](public-dashboard.md#stat)|   [PublicDashboardStatQuery](public-dashboard.md#publicdashboardstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** cost-analysis/v1/public-dashboard/create
>

> Creates a new PublicDashboard. This method is used for creating the default dashboard . `Admin` type Users can use the method to add a new dashboard with customized widgets.

| Type | Message |
| :--- | :--- |
| Request | [CreatePublicDashboardRequest](public-dashboard.md#createpublicdashboardrequest) |
| Response |  [PublicDashboardInfo](public-dashboard.md#publicdashboardinfo)  |
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
                    "chart_type": "LINE",
                    "layout": 100.0,
                    "chart_img": "AWS_Data-Transfer_Cost_Trend",
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_COST_TREND_DESC"
                }
            }
        ],
        [
            {
                "name": "AWS Data-Transfer by Region",
                "widget_id": "map-lg-02",
                "options": {
                    "chart_type": "MAP",
                    "layout": 100.0,
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_BY_REGION_DESC",
                    "chart_img": "AWS_Data-Transfer_By_Region"
                }
            }
        ],
        [
            {
                "name": "AWS CloudFront Cost by Project",
                "widget_id": "stackedcol-lg-03",
                "options": {
                    "group_by": "project_id",
                    "chart_img": "AWS_CloudFront_Cost",
                    "layout": 100.0,
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_CLOUDFRONT_COST_DESC",
                    "chart_type": "STACKED_COLUMN"
                }
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
    "public_dashboard_id": "pub-dash-80092b5ef658",
    "name": "Untitled Dashboard",
    "custom_layouts": [
        [
            {
                "options": {
                    "layout": 100.0,
                    "chart_type": "LINE",
                    "chart_img": "AWS_Data-Transfer_Cost_Trend",
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_COST_TREND_DESC"
                },
                "widget_id": "linegraph-lg-02",
                "name": "AWS Data-Transfer Cost Trend"
            }
        ],
        [
            {
                "widget_id": "map-lg-02",
                "name": "AWS Data-Transfer by Region",
                "options": {
                    "layout": 100.0,
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_BY_REGION_DESC",
                    "chart_img": "AWS_Data-Transfer_By_Region",
                    "chart_type": "MAP"
                }
            }
        ],
        [
            {
                "options": {
                    "chart_type": "STACKED_COLUMN",
                    "chart_img": "AWS_CloudFront_Cost",
                    "layout": 100.0,
                    "group_by": "project_id",
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_CLOUDFRONT_COST_DESC"
                },
                "name": "AWS CloudFront Cost by Project",
                "widget_id": "stackedcol-lg-03"
            }
        ]
    ],
    "default_filter": {},
    "period_type": "AUTO",
    "tags": {},
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-19T05:42:01.412Z",
    "updated_at": "2022-07-19T05:42:01.412Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **POST** cost-analysis/v1/public-dashboard/update
>

> Updates a specific PublicDashboard. Changes the widgets of the PublicDashboard with default widgets and customized widgets. Only `Admin` type Users can use the method.

| Type | Message |
| :--- | :--- |
| Request | [UpdatePublicDashboardRequest](public-dashboard.md#updatepublicdashboardrequest) |
| Response |  [PublicDashboardInfo](public-dashboard.md#publicdashboardinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "public_dashboard_id": "pub-dash-80092b5ef658",
    "name": "Untitled Dashboard2",
    "custom_layouts": [
        [
            {
                "widget_id": "linegraph-lg-02",
                "name": "AWS Data-Transfer Cost Trend",
                "options": {
                    "chart_type": "LINE",
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_COST_TREND_DESC",
                    "chart_img": "AWS_Data-Transfer_Cost_Trend",
                    "layout": 100.0
                }
            }
        ],
        [
            {
                "name": "AWS Data-Transfer by Region",
                "widget_id": "map-lg-02",
                "options": {
                    "chart_type": "MAP",
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_BY_REGION_DESC",
                    "layout": 100.0,
                    "chart_img": "AWS_Data-Transfer_By_Region"
                }
            }
        ],
        [
            {
                "name": "AWS CloudFront Cost by Project",
                "widget_id": "stackedcol-lg-03",
                "options": {
                    "layout": 100.0,
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_CLOUDFRONT_COST_DESC",
                    "group_by": "project_id",
                    "chart_type": "STACKED_COLUMN",
                    "chart_img": "AWS_CloudFront_Cost"
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
    "public_dashboard_id": "pub-dash-80092b5ef658",
    "name": "Untitled Dashboard2",
    "custom_layouts": [
        [
            {
                "options": {
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_COST_TREND_DESC",
                    "layout": 100.0,
                    "chart_type": "LINE",
                    "chart_img": "AWS_Data-Transfer_Cost_Trend"
                },
                "name": "AWS Data-Transfer Cost Trend",
                "widget_id": "linegraph-lg-02"
            }
        ],
        [
            {
                "options": {
                    "chart_type": "MAP",
                    "layout": 100.0,
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_BY_REGION_DESC",
                    "chart_img": "AWS_Data-Transfer_By_Region"
                },
                "widget_id": "map-lg-02",
                "name": "AWS Data-Transfer by Region"
            }
        ],
        [
            {
                "name": "AWS CloudFront Cost by Project",
                "widget_id": "stackedcol-lg-03",
                "options": {
                    "chart_img": "AWS_CloudFront_Cost",
                    "chart_type": "STACKED_COLUMN",
                    "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_CLOUDFRONT_COST_DESC",
                    "layout": 100.0,
                    "group_by": "project_id"
                }
            }
        ]
    ],
    "default_filter": {},
    "period_type": "AUTO",
    "tags": {},
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-19T05:42:01.412Z",
    "updated_at": "2022-07-19T05:42:01.412Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **POST** cost-analysis/v1/public-dashboard/delete
>

> Deletes a specific PublicDashboard. You must specify the `public_dashboard_id` of the PublicDashboard to delete.

| Type | Message |
| :--- | :--- |
| Request | [PublicDashboardRequest](public-dashboard.md#publicdashboardrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "public_dashboard_id": "pub-dash-579b38f00dcf"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **POST** cost-analysis/v1/public-dashboard/get
>

> Gets a specific PublicDashboard. Prints detailed information about the PublicDashboard, including `custom_layouts` and `period_type`.

| Type | Message |
| :--- | :--- |
| Request | [GetPublicDashboardRequest](public-dashboard.md#getpublicdashboardrequest) |
| Response |  [PublicDashboardInfo](public-dashboard.md#publicdashboardinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "public_dashboard_id": "pub-dash-579b38f00dcf"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "public_dashboard_id": "pub-dash-579b38f00dcf",
    "name": "CDN & Traffic Cost",
    "custom_layouts": [
        [
            {
                "name": "AWS Data-Transfer Cost Trend",
                "widget_id": "linegraph-lg-02",
                "options": {
                    "chart_type": "LINE",
                    "layout": 100.0
                }
            }
        ],
        [
            {
                "options": {
                    "layout": 100.0,
                    "group_by": "project_id",
                    "chart_type": "STACKED_COLUMN"
                },
                "name": "AWS CloudFront Cost by Project",
                "widget_id": "stackedcol-lg-03"
            }
        ],
        [
            {
                "widget_id": "map-lg-02",
                "name": "AWS Data-Transfer by Region",
                "options": {
                    "layout": 100.0,
                    "chart_type": "MAP"
                }
            }
        ]
    ],
    "default_filter": {
        "project_group_id": [],
        "service_account_id": [],
        "project_id": [],
        "provider": [
            "google_cloud",
            "azure",
            "aws_china",
            "aws"
        ]
    },
    "period_type": "AUTO",
    "tags": {},
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-04-07T02:31:28.197Z",
    "updated_at": "2022-04-07T02:31:28.197Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **POST** /cost-analysis/v1/public-dashboard/list
>

> Gets a list of all PublicDashboards. You can use a query to get a filtered list of PublicDashboards.

| Type | Message |
| :--- | :--- |
| Request | [PublicDashboardQuery](public-dashboard.md#publicdashboardquery) |
| Response |  [PublicDashboardsInfo](public-dashboard.md#publicdashboardsinfo)  |
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
            "public_dashboard_id": "pub-dash-579b38f00dcf",
            "name": "CDN & Traffic Cost",
            "custom_layouts": [
                [
                    {
                        "widget_id": "linegraph-lg-02",
                        "name": "AWS Data-Transfer Cost Trend",
                        "options": {
                            "chart_type": "LINE",
                            "layout": 100.0
                        }
                    }
                ],
                [
                    {
                        "name": "AWS CloudFront Cost by Project",
                        "options": {
                            "group_by": "project_id",
                            "chart_type": "STACKED_COLUMN",
                            "layout": 100.0
                        },
                        "widget_id": "stackedcol-lg-03"
                    }
                ],
                [
                    {
                        "options": {
                            "layout": 100.0,
                            "chart_type": "MAP"
                        },
                        "widget_id": "map-lg-02",
                        "name": "AWS Data-Transfer by Region"
                    }
                ]
            ],
            "default_filter": {
                "project_id": [],
                "service_account_id": [],
                "project_group_id": [],
                "provider": [
                    "google_cloud",
                    "azure",
                    "aws_china",
                    "aws"
                ]
            },
            "period_type": "AUTO",
            "tags": {},
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-04-07T02:31:28.197Z",
            "updated_at": "2022-04-07T02:31:28.197Z"
        },
        {
            "public_dashboard_id": "pub-dash-fc83ed9bc825",
            "name": "Monthly Cost Summary",
            "custom_layouts": [
                [
                    {
                        "options": {
                            "layout": 33.0,
                            "chart_type": "CARD"
                        },
                        "widget_id": "card-sm-01",
                        "name": "Month-to-Date Spend"
                    },
                    {
                        "name": "Last Month Total Spend",
                        "widget_id": "card-sm-02",
                        "options": {
                            "layout": 33.0,
                            "chart_type": "CARD"
                        }
                    },
                    {
                        "widget_id": "card-sm-03",
                        "name": "Budget Usage",
                        "options": {
                            "chart_type": "CARD",
                            "layout": 33.0
                        }
                    }
                ],
                [
                    {
                        "name": "Cost By Project",
                        "widget_id": "treemap-lg-01",
                        "options": {
                            "group_by": "project_id",
                            "layout": 100.0,
                            "chart_type": "TREEMAP"
                        }
                    }
                ],
                [
                    {
                        "name": "Cost Trend By Project",
                        "widget_id": "linegraph-lg-01",
                        "options": {
                            "layout": 100.0,
                            "group_by": "provider",
                            "chart_type": "LINE"
                        }
                    }
                ],
                [
                    {
                        "options": {
                            "layout": 100.0,
                            "chart_type": "STACKED_COLUMN",
                            "group_by": "product"
                        },
                        "widget_id": "stackedcol-lg-01",
                        "name": "Cost Trend By Product"
                    }
                ],
                [
                    {
                        "name": "Cost By Provider",
                        "options": {
                            "layout": 50.0,
                            "group_by": "provider",
                            "chart_type": "STACKED_COLUMN"
                        },
                        "widget_id": "donut-md-01"
                    },
                    {
                        "widget_id": "waffle-md-01",
                        "name": "Budget Status",
                        "options": {
                            "layout": 50.0,
                            "chart_type": "WAFFLE"
                        }
                    }
                ],
                [
                    {
                        "options": {
                            "chart_type": "MAP",
                            "layout": 100.0
                        },
                        "widget_id": "map-lg-01",
                        "name": "Cost By Region"
                    }
                ]
            ],
            "default_filter": {
                "provider": []
            },
            "period_type": "AUTO",
            "tags": {},
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-03-29T05:22:41.283Z",
            "updated_at": "2022-03-29T05:22:41.283Z"
        }
    ],
    "total_count": 3
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /cost-analysis/v1/public-dashboard/stat
>


| Type | Message |
| :--- | :--- |
| Request | [PublicDashboardStatQuery](public-dashboard.md#publicdashboardstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreatePublicDashboardRequest
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
      <td style="text-align:left"><a href="public-dashboard.md#publicdashboardperiod">PublicDashboardPeriod</a></td>
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



### GetPublicDashboardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| public_dashboard_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### PublicDashboardInfo
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
      <td style="text-align:left; width:100px;">public_dashboard_id</td>
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
      <td style="text-align:left"><a href="public-dashboard.md#publicdashboardperiod">PublicDashboardPeriod</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
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



### PublicDashboardPeriod
| Field | Type |  Description |
| :--- | :--- | :--- |
| start |string | |
| end |string | |

### PublicDashboardQuery
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
      <td style="text-align:left; width:100px;">public_dashboard_id</td>
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
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### PublicDashboardRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| public_dashboard_id |string|✔| |
| domain_id |string|✔| |

### PublicDashboardStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### PublicDashboardsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of PublicDashboardInfo](public-dashboard.md#publicdashboardinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdatePublicDashboardRequest
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
      <td style="text-align:left; width:100px;">public_dashboard_id</td>
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
      <td style="text-align:left"><a href="public-dashboard.md#publicdashboardperiod">PublicDashboardPeriod</a></td>
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


