
# 📊 Analytics Data Platform — Bronze → Silver → Gold Architecture

## Overview

This project implements a **modern analytics data platform** designed to ingest raw operational and marketing data, standardize and conform it, and expose **business-ready datasets** for BI, reporting, and downstream analytics.

The architecture follows a **Bronze → Silver → Gold** layered approach to ensure:

- Data correctness and traceability
- Clear ownership of transformations
- Scalable, maintainable analytics models
- Reliable BI consumption (Looker Studio)

The platform is intentionally **BI-first**, designed to prevent common analytics failures such as double counting, fan-out joins, and inconsistent metrics.

---

## Data Sources

### CRM

Operational data covering:

- Users
- Orders
- Events
- Payments
- Referrals
- Geographic attributes

**Input format:** Parquet
**Interface:** File-based ingestion (batch)

---

### Marketing

Marketing and growth data including:

- Campaigns and promotions
- Marketing spend
- Coupon redemptions
- Attribution data

**Input format:** Parquet
**Interface:** File-based ingestion (batch)

---

## Architecture Principles

- **Batch-first analytics** (not OLTP workloads)
- **Layered responsibility** — each layer has a single, well-defined purpose
- **Grain enforcement** before BI exposure
- **Star schema modeling** at the Gold layer
- **Zero business logic in BI tools**

---

## 🟫 Bronze Layer — Raw Ingestion

### Purpose

The Bronze layer stores **raw, immutable data** exactly as received from source systems.

### Characteristics

- No transformations
- No deduplication
- No business rules
- Schema mirrors the source structure
- Acts as the system of record

### Known Data Quality Issues (Intentionally Preserved)

Data profiling of the Bronze layer revealed several production-grade data issues commonly found in operational and marketing systems. These issues are **not corrected at this layer by design**.

#### 1. Identifier Inconsistencies
- Entity identifiers (e.g., `user_id`, `order_id`, `device_id`, `campaign_id`) are stored as strings
- Mixed identifier lengths and numeric-like values
- No enforced uniqueness or primary keys

**Impact:**  
Joins are unsafe at this layer and can easily result in fan-out errors.

---

#### 2. Duplicate Natural Keys
- Multiple rows may represent the same logical entity
- No guaranteed uniqueness constraints
- No reliable ordering or precedence logic in raw data

**Impact:**  
Direct aggregation can lead to double counting and inflated metrics.

---

#### 3. Missing and Partially Populated Fields
- Nullable fields across enrichment attributes, device metadata, and optional dimensions
- Records may be structurally valid but analytically incomplete

**Impact:**  
Unstable segmentation and unreliable filtering if consumed directly.

---

#### 4. Undefined or Mixed Grain
- Event-level, transaction-level, and entity-level records coexist
- Grain is implicit and not enforced

**Impact:**  
Aggregations are ambiguous and analytically unsafe without downstream modeling.

---

#### 5. Non-standardized Categorical Values
- Free-text values for status, type, channel, and category fields
- No canonical reference dimensions

**Impact:**  
Inconsistent groupings and unreliable BI outputs.

---

#### 6. Temporal Ambiguity
- Multiple date and timestamp fields per dataset
- No single canonical business time defined

**Impact:**  
Inconsistent time-based reporting and misleading trend analysis.

---

#### 7. Source-Coupled Schemas
- Table structures reflect upstream operational systems
- Not designed for analytical querying or BI consumption

**Impact:**  
Direct BI usage would be fragile, slow, and error-prone.

---

### Object Type

- Tables

### Load Strategy

- Full loads
- Truncate & insert (source dependent)
- Batch processing

### Examples

- `bronze_users`
- `bronze_orders`
- `bronze_events`
- `bronze_marketing_cost`
- `bronze_promotions`

---

> **Design Intent:**  
> The Bronze layer is **deliberately not analytics-ready**.  
> All identified data issues are resolved in the Silver layer and structurally prevented in the Gold layer.

> Bronze answers: *“What did the source system send?”*

---

## 🩶 Silver Layer — Clean & Conformed Data

### Purpose

The Silver layer prepares data for analytics by enforcing **data quality, consistency, and correct grain**.

### Transformations Applied

- Column renaming and standardization
- Data type normalization
- Deduplication
- Grain enforcement
- Referential integrity checks
- Derived technical columns
- Dataset enrichment

### Object Type

- Tables

### Load Strategy

- Incremental loads
- Insert / merge logic
- Idempotent processing

### Examples

- `silver_users`
- `silver_orders`
- `silver_order_items`
- `silver_events`
- `silver_marketing_cost`
- `silver_marketing_attribution`

> Silver answers: *“What is the clean, trusted version of the data?”*

---

## 🟨 Gold Layer — Business-Ready Analytics

### Purpose

The Gold layer exposes **analytics-ready datasets** designed explicitly for BI tools and decision-making.

This layer contains:

- Fact tables with explicit grains
- Dimension tables for slicing and filtering
- Centrally defined, trusted metrics

### Key Design Rules

- One fact table = one grain
- No cross-grain joins
- No metric logic in BI tools
- No raw or semi-processed data exposed

### Object Types

- Views (preferred)
- Aggregated fact tables (when required)

### Data Modeling

- Star schema
- Clear fact / dimension separation
- Explicit surrogate and natural keys

### Examples

#### Dimensions

- `gold_dim_date`
- `gold_dim_user`
- `gold_dim_device`
- `gold_dim_geo`
- `gold_dim_channel`
- `gold_dim_promotion`
- `gold_dim_provider`

#### Facts

- `gold_fact_events`
- `gold_fact_orders`
- `gold_user_value_profile`

> Gold answers: *“What does the business need to measure?”*

---

## 📈 BI & Consumption Layer

### Tooling

- **Looker Studio**

### Access Pattern

- One Looker data source per Gold fact table
- No blending of fact tables
- Metrics defined centrally in the warehouse

### Outcomes

- Stable dashboards
- Predictable, explainable numbers
- No metric drift
- Consistent performance

---

## 🤖 Downstream & Advanced Use Cases

The Gold layer is also designed to support:

- Feature engineering
- User value modeling
- Machine learning pipelines
- Advanced segmentation and cohort analysis

---

## Why This Architecture Works

- Prevents double counting and fan-out errors
- Scales cleanly with data growth
- Separates technical and business concerns
- Reduces BI maintenance overhead
- Builds long-term trust in analytics

---

## Summary

This project demonstrates a strong **analytics engineering mindset**, where:

- Data modeling is intentional
- BI tools are consumers — not calculators
- Architectural decisions directly protect metric integrity

The platform is built to evolve:
new sources, facts, and dimensions can be added **without breaking existing analytics**.

---

## Tooling & Infrastructure

- **PySpark** — transformation and processing
- **MySQL** — analytical storage
- **Docker** — environment consistency
- **VPS-hosted database** — BI connectivity (Looker Studio & other BI tools)
- **draw.io** — data architecture and pipeline design diagrams (Bronze → Silver → Gold)
