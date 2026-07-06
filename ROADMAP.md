# Roadmap — O*NET occupation checklist

Master backlog of human expert roles to eventually cover in this repo, sourced from the U.S. Department of Labor's [O*NET database](https://www.onetcenter.org/database.html) (public domain, CC-licensed, release 30.3), which covers 1,016 detailed occupations across 23 major groups.

This is the checklist, not a commitment — it exists so contributors can see what's uncovered and claim a role via PR instead of duplicating effort or guessing what's missing. O*NET is US-centric and salaried-employment-framed; it's a strong systematic backbone but not the only valid source of roles (see "Roles outside this list" at the bottom).

**Status legend:** ✅ drafted at current spec · ♻️ drafted, awaiting spec-2 upgrade (see [Spec-2 upgrade queue](#spec-2-upgrade-queue)) · *(blank)* not started

**Progress: 155 / 1016 O*NET occupations drafted · 42 drafted roles awaiting spec-2 upgrade.**

<!-- CHECKLIST START -->

<details>
<summary><strong>11 — Management</strong> (57/59 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
| ♻️ | 11-1011.00 | Chief Executives | [`chief-executive`](./roles/chief-executive/SKILL.md) |
| ♻️ | 11-1011.03 | Chief Sustainability Officers | [`chief-sustainability-officer`](./roles/chief-sustainability-officer/SKILL.md) |
| ♻️ | 11-1021.00 | General and Operations Managers | [`general-operations-manager`](./roles/general-operations-manager/SKILL.md) |
| ♻️ | 11-1031.00 | Legislators | [`legislator`](./roles/legislator/SKILL.md) |
| ♻️ | 11-2011.00 | Advertising and Promotions Managers | [`advertising-promotions-manager`](./roles/advertising-promotions-manager/SKILL.md) |
| ♻️ | 11-2021.00 | Marketing Managers | [`marketing-manager`](./roles/marketing-manager/SKILL.md) |
| ♻️ | 11-2022.00 | Sales Managers | [`sales-manager`](./roles/sales-manager/SKILL.md) |
| ♻️ | 11-2032.00 | Public Relations Managers | [`public-relations-manager`](./roles/public-relations-manager/SKILL.md) |
| ♻️ | 11-2033.00 | Fundraising Managers | [`fundraising-manager`](./roles/fundraising-manager/SKILL.md) |
| ♻️ | 11-3012.00 | Administrative Services Managers | [`administrative-services-manager`](./roles/administrative-services-manager/SKILL.md) |
| ♻️ | 11-3013.00 | Facilities Managers | [`facilities-manager`](./roles/facilities-manager/SKILL.md) |
| ♻️ | 11-3013.01 | Security Managers | [`security-manager`](./roles/security-manager/SKILL.md) |
| ♻️ | 11-3021.00 | Computer and Information Systems Managers | [`computer-information-systems-manager`](./roles/computer-information-systems-manager/SKILL.md) |
| ✅ | 11-3031.00 | Financial Managers | [`financial-manager`](./roles/financial-manager/SKILL.md) |
| ♻️ | 11-3031.01 | Treasurers and Controllers | [`treasurer-controller`](./roles/treasurer-controller/SKILL.md) |
| ♻️ | 11-3031.03 | Investment Fund Managers | [`investment-fund-manager`](./roles/investment-fund-manager/SKILL.md) |
| ♻️ | 11-3051.00 | Industrial Production Managers | [`industrial-production-manager`](./roles/industrial-production-manager/SKILL.md) |
| ♻️ | 11-3051.01 | Quality Control Systems Managers | [`quality-control-systems-manager`](./roles/quality-control-systems-manager/SKILL.md) |
| ♻️ | 11-3051.02 | Geothermal Production Managers | [`geothermal-production-manager`](./roles/geothermal-production-manager/SKILL.md) |
| ♻️ | 11-3051.03 | Biofuels Production Managers | [`biofuels-production-manager`](./roles/biofuels-production-manager/SKILL.md) |
| ♻️ | 11-3051.04 | Biomass Power Plant Managers | [`biomass-power-plant-manager`](./roles/biomass-power-plant-manager/SKILL.md) |
| ♻️ | 11-3051.06 | Hydroelectric Production Managers | [`hydroelectric-production-manager`](./roles/hydroelectric-production-manager/SKILL.md) |
| ♻️ | 11-3061.00 | Purchasing Managers | [`purchasing-manager`](./roles/purchasing-manager/SKILL.md) |
| ♻️ | 11-3071.00 | Transportation, Storage, and Distribution Managers | [`transportation-storage-distribution-manager`](./roles/transportation-storage-distribution-manager/SKILL.md) |
| ♻️ | 11-3071.04 | Supply Chain Managers | [`supply-chain-manager`](./roles/supply-chain-manager/SKILL.md) |
| ♻️ | 11-3111.00 | Compensation and Benefits Managers | [`compensation-benefits-manager`](./roles/compensation-benefits-manager/SKILL.md) |
| ♻️ | 11-3121.00 | Human Resources Managers | [`hr-people-manager`](./roles/hr-people-manager/SKILL.md) |
| ♻️ | 11-3131.00 | Training and Development Managers | [`training-development-manager`](./roles/training-development-manager/SKILL.md) |
| ♻️ | 11-9013.00 | Farmers, Ranchers, and Other Agricultural Managers | [`agricultural-manager`](./roles/agricultural-manager/SKILL.md) |
| ♻️ | 11-9021.00 | Construction Managers | [`construction-manager`](./roles/construction-manager/SKILL.md) |
| ♻️ | 11-9031.00 | Education and Childcare Administrators, Preschool and Daycare | [`education-childcare-administrator-preschool`](./roles/education-childcare-administrator-preschool/SKILL.md) |
| ♻️ | 11-9032.00 | Education Administrators, Kindergarten through Secondary | [`education-administrator-k12`](./roles/education-administrator-k12/SKILL.md) |
| ♻️ | 11-9033.00 | Education Administrators, Postsecondary | [`education-administrator-postsecondary`](./roles/education-administrator-postsecondary/SKILL.md) |
| ♻️ | 11-9039.00 | Education Administrators, All Other | [`education-administrator-other`](./roles/education-administrator-other/SKILL.md) |
| ✅ | 11-9041.00 | Architectural and Engineering Managers | [`architectural-engineering-manager`](./roles/architectural-engineering-manager/SKILL.md) |
| ✅ | 11-9041.01 | Biofuels/Biodiesel Technology and Product Development Managers | [`biofuels-biodiesel-technology-manager`](./roles/biofuels-biodiesel-technology-manager/SKILL.md) |
| ✅ | 11-9051.00 | Food Service Managers | [`food-service-manager`](./roles/food-service-manager/SKILL.md) |
| ✅ | 11-9071.00 | Gambling Managers | [`gambling-manager`](./roles/gambling-manager/SKILL.md) |
| ✅ | 11-9072.00 | Entertainment and Recreation Managers, Except Gambling | [`entertainment-recreation-manager`](./roles/entertainment-recreation-manager/SKILL.md) |
| ✅ | 11-9081.00 | Lodging Managers | [`lodging-manager`](./roles/lodging-manager/SKILL.md) |
| ✅ | 11-9111.00 | Medical and Health Services Managers | [`medical-health-services-manager`](./roles/medical-health-services-manager/SKILL.md) |
| ✅ | 11-9121.00 | Natural Sciences Managers | [`natural-sciences-manager`](./roles/natural-sciences-manager/SKILL.md) |
| ✅ | 11-9121.01 | Clinical Research Coordinators | [`clinical-research-coordinator`](./roles/clinical-research-coordinator/SKILL.md) |
| ✅ | 11-9121.02 | Water Resource Specialists | [`water-resource-specialist`](./roles/water-resource-specialist/SKILL.md) |
| ✅ | 11-9131.00 | Postmasters and Mail Superintendents | [`postmaster-mail-superintendent`](./roles/postmaster-mail-superintendent/SKILL.md) |
| ✅ | 11-9141.00 | Property, Real Estate, and Community Association Managers | [`property-real-estate-manager`](./roles/property-real-estate-manager/SKILL.md) |
| ✅ | 11-9151.00 | Social and Community Service Managers | [`social-community-service-manager`](./roles/social-community-service-manager/SKILL.md) |
| ✅ | 11-9161.00 | Emergency Management Directors | [`emergency-management-director`](./roles/emergency-management-director/SKILL.md) |
| ✅ | 11-9171.00 | Funeral Home Managers | [`funeral-home-manager`](./roles/funeral-home-manager/SKILL.md) |
|  | 11-9179.00 | Personal Service Managers, All Other |  |
| ✅ | 11-9179.01 | Fitness and Wellness Coordinators | [`fitness-wellness-coordinator`](./roles/fitness-wellness-coordinator/SKILL.md) |
| ✅ | 11-9179.02 | Spa Managers | [`spa-manager`](./roles/spa-manager/SKILL.md) |
|  | 11-9199.00 | Managers, All Other |  |
| ✅ | 11-9199.01 | Regulatory Affairs Managers | [`regulatory-affairs-manager`](./roles/regulatory-affairs-manager/SKILL.md) |
| ✅ | 11-9199.02 | Compliance Managers | [`compliance-manager`](./roles/compliance-manager/SKILL.md) |
| ✅ | 11-9199.08 | Loss Prevention Managers | [`loss-prevention-manager`](./roles/loss-prevention-manager/SKILL.md) |
| ✅ | 11-9199.09 | Wind Energy Operations Managers | [`wind-energy-operations-manager`](./roles/wind-energy-operations-manager/SKILL.md) |
| ✅ | 11-9199.10 | Wind Energy Development Managers | [`wind-energy-development-manager`](./roles/wind-energy-development-manager/SKILL.md) |
| ✅ | 11-9199.11 | Brownfield Redevelopment Specialists and Site Managers | [`brownfield-redevelopment-specialist`](./roles/brownfield-redevelopment-specialist/SKILL.md) |

</details>

<details>
<summary><strong>13 — Business and Financial Operations</strong> (45/50 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
| ✅ | 13-1011.00 | Agents and Business Managers of Artists, Performers, and Athletes | [`talent-agent`](./roles/talent-agent/SKILL.md) |
| ✅ | 13-1021.00 | Buyers and Purchasing Agents, Farm Products | [`farm-products-buyer`](./roles/farm-products-buyer/SKILL.md) |
| ✅ | 13-1022.00 | Wholesale and Retail Buyers, Except Farm Products | [`retail-buyer`](./roles/retail-buyer/SKILL.md) |
| ✅ | 13-1023.00 | Purchasing Agents, Except Wholesale, Retail, and Farm Products | [`purchasing-agent`](./roles/purchasing-agent/SKILL.md) |
| ✅ | 13-1031.00 | Claims Adjusters, Examiners, and Investigators | [`claims-adjuster`](./roles/claims-adjuster/SKILL.md) |
| ✅ | 13-1032.00 | Insurance Appraisers, Auto Damage | [`auto-damage-appraiser`](./roles/auto-damage-appraiser/SKILL.md) |
| ✅ | 13-1041.00 | Compliance Officers | [`compliance-officer`](./roles/compliance-officer/SKILL.md) |
| ✅ | 13-1041.01 | Environmental Compliance Inspectors | [`environmental-compliance-inspector`](./roles/environmental-compliance-inspector/SKILL.md) |
| ✅ | 13-1041.03 | Equal Opportunity Representatives and Officers | [`equal-opportunity-representative`](./roles/equal-opportunity-representative/SKILL.md) |
| ✅ | 13-1041.04 | Government Property Inspectors and Investigators | [`government-property-inspector`](./roles/government-property-inspector/SKILL.md) |
| ✅ | 13-1041.06 | Coroners | [`coroner`](./roles/coroner/SKILL.md) |
|  | 13-1041.07 | Regulatory Affairs Specialists |  |
| ✅ | 13-1041.08 | Customs Brokers | [`customs-broker`](./roles/customs-broker/SKILL.md) |
| ✅ | 13-1051.00 | Cost Estimators | [`cost-estimator`](./roles/cost-estimator/SKILL.md) |
| ✅ | 13-1071.00 | Human Resources Specialists | [`hr-specialist`](./roles/hr-specialist/SKILL.md) |
| ✅ | 13-1074.00 | Farm Labor Contractors | [`farm-labor-contractor`](./roles/farm-labor-contractor/SKILL.md) |
| ✅ | 13-1075.00 | Labor Relations Specialists | [`labor-relations-specialist`](./roles/labor-relations-specialist/SKILL.md) |
| ✅ | 13-1081.00 | Logisticians | [`logistician`](./roles/logistician/SKILL.md) |
| ✅ | 13-1081.01 | Logistics Engineers | [`logistics-engineer`](./roles/logistics-engineer/SKILL.md) |
| ✅ | 13-1081.02 | Logistics Analysts | [`logistics-analyst`](./roles/logistics-analyst/SKILL.md) |
| ✅ | 13-1082.00 | Project Management Specialists | [`project-management-specialist`](./roles/project-management-specialist/SKILL.md) |
| ✅ | 13-1111.00 | Management Analysts | [`management-analyst`](./roles/management-analyst/SKILL.md) |
| ✅ | 13-1121.00 | Meeting, Convention, and Event Planners | [`meeting-event-planner`](./roles/meeting-event-planner/SKILL.md) |
|  | 13-1131.00 | Fundraisers |  |
| ✅ | 13-1141.00 | Compensation, Benefits, and Job Analysis Specialists | [`compensation-benefits-specialist`](./roles/compensation-benefits-specialist/SKILL.md) |
| ✅ | 13-1151.00 | Training and Development Specialists | [`training-development-specialist`](./roles/training-development-specialist/SKILL.md) |
| ✅ | 13-1161.00 | Market Research Analysts and Marketing Specialists | [`marketing-strategist`](./roles/marketing-strategist/SKILL.md) |
| ✅ | 13-1161.01 | Search Marketing Strategists | [`search-marketing-strategist`](./roles/search-marketing-strategist/SKILL.md) |
|  | 13-1199.00 | Business Operations Specialists, All Other |  |
| ✅ | 13-1199.04 | Business Continuity Planners | [`business-continuity-planner`](./roles/business-continuity-planner/SKILL.md) |
| ✅ | 13-1199.05 | Sustainability Specialists | [`sustainability-specialist`](./roles/sustainability-specialist/SKILL.md) |
| ✅ | 13-1199.06 | Online Merchants | [`online-merchant`](./roles/online-merchant/SKILL.md) |
|  | 13-1199.07 | Security Management Specialists |  |
| ♻️ | 13-2011.00 | Accountants and Auditors | [`accountant-controller`](./roles/accountant-controller/SKILL.md) |
| ✅ | 13-2022.00 | Appraisers of Personal and Business Property | [`personal-property-appraiser`](./roles/personal-property-appraiser/SKILL.md) |
| ✅ | 13-2023.00 | Appraisers and Assessors of Real Estate | [`real-estate-appraiser`](./roles/real-estate-appraiser/SKILL.md) |
| ✅ | 13-2031.00 | Budget Analysts | [`budget-analyst`](./roles/budget-analyst/SKILL.md) |
| ✅ | 13-2041.00 | Credit Analysts | [`credit-analyst`](./roles/credit-analyst/SKILL.md) |
| ♻️ | 13-2051.00 | Financial and Investment Analysts | [`financial-analyst`](./roles/financial-analyst/SKILL.md) |
| ✅ | 13-2052.00 | Personal Financial Advisors | [`personal-financial-advisor`](./roles/personal-financial-advisor/SKILL.md) |
| ✅ | 13-2053.00 | Insurance Underwriters | [`insurance-underwriter`](./roles/insurance-underwriter/SKILL.md) |
| ✅ | 13-2054.00 | Financial Risk Specialists | [`financial-risk-specialist`](./roles/financial-risk-specialist/SKILL.md) |
| ✅ | 13-2061.00 | Financial Examiners | [`financial-examiner`](./roles/financial-examiner/SKILL.md) |
| ✅ | 13-2071.00 | Credit Counselors | [`credit-counselor`](./roles/credit-counselor/SKILL.md) |
| ✅ | 13-2072.00 | Loan Officers | [`loan-officer`](./roles/loan-officer/SKILL.md) |
| ✅ | 13-2081.00 | Tax Examiners and Collectors, and Revenue Agents | [`tax-revenue-agent`](./roles/tax-revenue-agent/SKILL.md) |
| ✅ | 13-2082.00 | Tax Preparers | [`tax-preparer`](./roles/tax-preparer/SKILL.md) |
|  | 13-2099.00 | Financial Specialists, All Other |  |
| ✅ | 13-2099.01 | Financial Quantitative Analysts | [`financial-quantitative-analyst`](./roles/financial-quantitative-analyst/SKILL.md) |
| ✅ | 13-2099.04 | Fraud Examiners, Investigators and Analysts | [`fraud-examiner`](./roles/fraud-examiner/SKILL.md) |

</details>

<details>
<summary><strong>15 — Computer and Mathematical</strong> (26/38 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
| ✅ | 15-1211.00 | Computer Systems Analysts | [`computer-systems-analyst`](./roles/computer-systems-analyst/SKILL.md) |
| ✅ | 15-1211.01 | Health Informatics Specialists | [`health-informatics-specialist`](./roles/health-informatics-specialist/SKILL.md) |
| ✅ | 15-1212.00 | Information Security Analysts | [`information-security-analyst`](./roles/information-security-analyst/SKILL.md) |
| ✅ | 15-1221.00 | Computer and Information Research Scientists | [`computer-information-research-scientist`](./roles/computer-information-research-scientist/SKILL.md) |
| ✅ | 15-1231.00 | Computer Network Support Specialists | [`network-support-specialist`](./roles/network-support-specialist/SKILL.md) |
| ✅ | 15-1232.00 | Computer User Support Specialists | [`computer-user-support-specialist`](./roles/computer-user-support-specialist/SKILL.md) |
| ✅ | 15-1241.00 | Computer Network Architects | [`network-architect`](./roles/network-architect/SKILL.md) |
| ✅ | 15-1241.01 | Telecommunications Engineering Specialists | [`telecommunications-engineering-specialist`](./roles/telecommunications-engineering-specialist/SKILL.md) |
| ✅ | 15-1242.00 | Database Administrators | [`database-administrator`](./roles/database-administrator/SKILL.md) |
| ✅ | 15-1243.00 | Database Architects | [`database-architect`](./roles/database-architect/SKILL.md) |
| ✅ | 15-1243.01 | Data Warehousing Specialists | [`data-warehousing-specialist`](./roles/data-warehousing-specialist/SKILL.md) |
| ✅ | 15-1244.00 | Network and Computer Systems Administrators | [`network-systems-administrator`](./roles/network-systems-administrator/SKILL.md) |
|  | 15-1251.00 | Computer Programmers |  |
| ♻️ | 15-1252.00 | Software Developers | [`software-engineer`](./roles/software-engineer/SKILL.md) |
| ✅ | 15-1253.00 | Software Quality Assurance Analysts and Testers | [`software-qa-analyst`](./roles/software-qa-analyst/SKILL.md) |
| ✅ | 15-1254.00 | Web Developers | [`full-stack-developer`](./roles/full-stack-developer/SKILL.md) |
| ♻️ | 15-1255.00 | Web and Digital Interface Designers | [`ux-designer`](./roles/ux-designer/SKILL.md) |
| ✅ | 15-1255.01 | Video Game Designers | [`game-designer`](./roles/game-designer/SKILL.md) |
|  | 15-1299.00 | Computer Occupations, All Other |  |
|  | 15-1299.01 | Web Administrators |  |
| ✅ | 15-1299.02 | Geographic Information Systems Technologists and Technicians | [`gis-technologist`](./roles/gis-technologist/SKILL.md) |
|  | 15-1299.03 | Document Management Specialists |  |
| ✅ | 15-1299.04 | Penetration Testers | [`penetration-tester`](./roles/penetration-tester/SKILL.md) |
| ✅ | 15-1299.05 | Information Security Engineers | [`application-security-engineer`](./roles/application-security-engineer/SKILL.md) |
| ✅ | 15-1299.06 | Digital Forensics Analysts | [`digital-forensics-analyst`](./roles/digital-forensics-analyst/SKILL.md) |
| ✅ | 15-1299.07 | Blockchain Engineers | [`blockchain-engineer`](./roles/blockchain-engineer/SKILL.md) |
|  | 15-1299.08 | Computer Systems Engineers/Architects |  |
|  | 15-1299.09 | Information Technology Project Managers |  |
| ✅ | 15-2011.00 | Actuaries | [`actuary`](./roles/actuary/SKILL.md) |
| ✅ | 15-2021.00 | Mathematicians | [`mathematician`](./roles/mathematician/SKILL.md) |
| ✅ | 15-2031.00 | Operations Research Analysts | [`operations-research-analyst`](./roles/operations-research-analyst/SKILL.md) |
|  | 15-2041.00 | Statisticians |  |
|  | 15-2041.01 | Biostatisticians |  |
| ✅ | 15-2051.00 | Data Scientists | [`data-scientist`](./roles/data-scientist/SKILL.md) |
|  | 15-2051.01 | Business Intelligence Analysts |  |
|  | 15-2051.02 | Clinical Data Managers |  |
|  | 15-2099.00 | Mathematical Science Occupations, All Other |  |
|  | 15-2099.01 | Bioinformatics Technicians |  |

</details>

<details>
<summary><strong>17 — Architecture and Engineering</strong> (2/59 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
|  | 17-1011.00 | Architects, Except Landscape and Naval |  |
|  | 17-1012.00 | Landscape Architects |  |
|  | 17-1021.00 | Cartographers and Photogrammetrists |  |
|  | 17-1022.00 | Surveyors |  |
|  | 17-1022.01 | Geodetic Surveyors |  |
|  | 17-2011.00 | Aerospace Engineers |  |
|  | 17-2021.00 | Agricultural Engineers |  |
|  | 17-2031.00 | Bioengineers and Biomedical Engineers |  |
|  | 17-2041.00 | Chemical Engineers |  |
| ✅ | 17-2051.00 | Civil Engineers | [`civil-engineer`](./roles/civil-engineer/SKILL.md) |
|  | 17-2051.01 | Transportation Engineers |  |
|  | 17-2051.02 | Water/Wastewater Engineers |  |
|  | 17-2061.00 | Computer Hardware Engineers |  |
|  | 17-2071.00 | Electrical Engineers |  |
|  | 17-2072.00 | Electronics Engineers, Except Computer |  |
|  | 17-2072.01 | Radio Frequency Identification Device Specialists |  |
|  | 17-2081.00 | Environmental Engineers |  |
|  | 17-2111.00 | Health and Safety Engineers, Except Mining Safety Engineers and Inspectors |  |
|  | 17-2111.02 | Fire-Prevention and Protection Engineers |  |
|  | 17-2112.00 | Industrial Engineers |  |
|  | 17-2112.01 | Human Factors Engineers and Ergonomists |  |
|  | 17-2112.02 | Validation Engineers |  |
|  | 17-2112.03 | Manufacturing Engineers |  |
|  | 17-2121.00 | Marine Engineers and Naval Architects |  |
|  | 17-2131.00 | Materials Engineers |  |
| ✅ | 17-2141.00 | Mechanical Engineers | [`mechanical-engineer`](./roles/mechanical-engineer/SKILL.md) |
|  | 17-2141.01 | Fuel Cell Engineers |  |
|  | 17-2141.02 | Automotive Engineers |  |
|  | 17-2151.00 | Mining and Geological Engineers, Including Mining Safety Engineers |  |
|  | 17-2161.00 | Nuclear Engineers |  |
|  | 17-2171.00 | Petroleum Engineers |  |
|  | 17-2199.00 | Engineers, All Other |  |
|  | 17-2199.03 | Energy Engineers, Except Wind and Solar |  |
|  | 17-2199.05 | Mechatronics Engineers |  |
|  | 17-2199.06 | Microsystems Engineers |  |
|  | 17-2199.07 | Photonics Engineers |  |
|  | 17-2199.08 | Robotics Engineers |  |
|  | 17-2199.09 | Nanosystems Engineers |  |
|  | 17-2199.10 | Wind Energy Engineers |  |
|  | 17-2199.11 | Solar Energy Systems Engineers |  |
|  | 17-3011.00 | Architectural and Civil Drafters |  |
|  | 17-3012.00 | Electrical and Electronics Drafters |  |
|  | 17-3013.00 | Mechanical Drafters |  |
|  | 17-3019.00 | Drafters, All Other |  |
|  | 17-3021.00 | Aerospace Engineering and Operations Technologists and Technicians |  |
|  | 17-3022.00 | Civil Engineering Technologists and Technicians |  |
|  | 17-3023.00 | Electrical and Electronic Engineering Technologists and Technicians |  |
|  | 17-3024.00 | Electro-Mechanical and Mechatronics Technologists and Technicians |  |
|  | 17-3024.01 | Robotics Technicians |  |
|  | 17-3025.00 | Environmental Engineering Technologists and Technicians |  |
|  | 17-3026.00 | Industrial Engineering Technologists and Technicians |  |
|  | 17-3026.01 | Nanotechnology Engineering Technologists and Technicians |  |
|  | 17-3027.00 | Mechanical Engineering Technologists and Technicians |  |
|  | 17-3027.01 | Automotive Engineering Technicians |  |
|  | 17-3028.00 | Calibration Technologists and Technicians |  |
|  | 17-3029.00 | Engineering Technologists and Technicians, Except Drafters, All Other |  |
|  | 17-3029.01 | Non-Destructive Testing Specialists |  |
|  | 17-3029.08 | Photonics Technicians |  |
|  | 17-3031.00 | Surveying and Mapping Technicians |  |

</details>

<details>
<summary><strong>19 — Life, Physical, and Social Science</strong> (0/66 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
|  | 19-1011.00 | Animal Scientists |  |
|  | 19-1012.00 | Food Scientists and Technologists |  |
|  | 19-1013.00 | Soil and Plant Scientists |  |
|  | 19-1021.00 | Biochemists and Biophysicists |  |
|  | 19-1022.00 | Microbiologists |  |
|  | 19-1023.00 | Zoologists and Wildlife Biologists |  |
|  | 19-1029.00 | Biological Scientists, All Other |  |
|  | 19-1029.01 | Bioinformatics Scientists |  |
|  | 19-1029.02 | Molecular and Cellular Biologists |  |
|  | 19-1029.03 | Geneticists |  |
|  | 19-1029.04 | Biologists |  |
|  | 19-1031.00 | Conservation Scientists |  |
|  | 19-1031.02 | Range Managers |  |
|  | 19-1031.03 | Park Naturalists |  |
|  | 19-1032.00 | Foresters |  |
|  | 19-1041.00 | Epidemiologists |  |
|  | 19-1042.00 | Medical Scientists, Except Epidemiologists |  |
|  | 19-1099.00 | Life Scientists, All Other |  |
|  | 19-2011.00 | Astronomers |  |
|  | 19-2012.00 | Physicists |  |
|  | 19-2021.00 | Atmospheric and Space Scientists |  |
|  | 19-2031.00 | Chemists |  |
|  | 19-2032.00 | Materials Scientists |  |
|  | 19-2041.00 | Environmental Scientists and Specialists, Including Health |  |
|  | 19-2041.01 | Climate Change Policy Analysts |  |
|  | 19-2041.02 | Environmental Restoration Planners |  |
|  | 19-2041.03 | Industrial Ecologists |  |
|  | 19-2042.00 | Geoscientists, Except Hydrologists and Geographers |  |
|  | 19-2043.00 | Hydrologists |  |
|  | 19-2099.00 | Physical Scientists, All Other |  |
|  | 19-2099.01 | Remote Sensing Scientists and Technologists |  |
|  | 19-3011.00 | Economists |  |
|  | 19-3011.01 | Environmental Economists |  |
|  | 19-3022.00 | Survey Researchers |  |
|  | 19-3032.00 | Industrial-Organizational Psychologists |  |
|  | 19-3033.00 | Clinical and Counseling Psychologists |  |
|  | 19-3034.00 | School Psychologists |  |
|  | 19-3039.00 | Psychologists, All Other |  |
|  | 19-3039.02 | Neuropsychologists |  |
|  | 19-3039.03 | Clinical Neuropsychologists |  |
|  | 19-3041.00 | Sociologists |  |
|  | 19-3051.00 | Urban and Regional Planners |  |
|  | 19-3091.00 | Anthropologists and Archeologists |  |
|  | 19-3092.00 | Geographers |  |
|  | 19-3093.00 | Historians |  |
|  | 19-3094.00 | Political Scientists |  |
|  | 19-3099.00 | Social Scientists and Related Workers, All Other |  |
|  | 19-3099.01 | Transportation Planners |  |
|  | 19-4012.00 | Agricultural Technicians |  |
|  | 19-4012.01 | Precision Agriculture Technicians |  |
|  | 19-4013.00 | Food Science Technicians |  |
|  | 19-4021.00 | Biological Technicians |  |
|  | 19-4031.00 | Chemical Technicians |  |
|  | 19-4042.00 | Environmental Science and Protection Technicians, Including Health |  |
|  | 19-4043.00 | Geological Technicians, Except Hydrologic Technicians |  |
|  | 19-4044.00 | Hydrologic Technicians |  |
|  | 19-4051.00 | Nuclear Technicians |  |
|  | 19-4051.02 | Nuclear Monitoring Technicians |  |
|  | 19-4061.00 | Social Science Research Assistants |  |
|  | 19-4071.00 | Forest and Conservation Technicians |  |
|  | 19-4092.00 | Forensic Science Technicians |  |
|  | 19-4099.00 | Life, Physical, and Social Science Technicians, All Other |  |
|  | 19-4099.01 | Quality Control Analysts |  |
|  | 19-4099.03 | Remote Sensing Technicians |  |
|  | 19-5011.00 | Occupational Health and Safety Specialists |  |
|  | 19-5012.00 | Occupational Health and Safety Technicians |  |

</details>

<details>
<summary><strong>21 — Community and Social Service</strong> (6/18 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
| ✅ | 21-1011.00 | Substance Abuse and Behavioral Disorder Counselors | [`substance-abuse-counselor`](./roles/substance-abuse-counselor/SKILL.md) |
| ✅ | 21-1012.00 | Educational, Guidance, and Career Counselors and Advisors | [`school-career-counselor`](./roles/school-career-counselor/SKILL.md) |
| ✅ | 21-1013.00 | Marriage and Family Therapists | [`marriage-family-therapist`](./roles/marriage-family-therapist/SKILL.md) |
| ✅ | 21-1014.00 | Mental Health Counselors | [`mental-health-counselor`](./roles/mental-health-counselor/SKILL.md) |
|  | 21-1015.00 | Rehabilitation Counselors |  |
|  | 21-1019.00 | Counselors, All Other |  |
| ✅ | 21-1021.00 | Child, Family, and School Social Workers | [`child-family-social-worker`](./roles/child-family-social-worker/SKILL.md) |
|  | 21-1022.00 | Healthcare Social Workers |  |
|  | 21-1023.00 | Mental Health and Substance Abuse Social Workers |  |
|  | 21-1029.00 | Social Workers, All Other |  |
|  | 21-1091.00 | Health Education Specialists |  |
| ✅ | 21-1092.00 | Probation Officers and Correctional Treatment Specialists | [`probation-officer`](./roles/probation-officer/SKILL.md) |
|  | 21-1093.00 | Social and Human Service Assistants |  |
|  | 21-1094.00 | Community Health Workers |  |
|  | 21-1099.00 | Community and Social Service Specialists, All Other |  |
|  | 21-2011.00 | Clergy |  |
|  | 21-2021.00 | Directors, Religious Activities and Education |  |
|  | 21-2099.00 | Religious Workers, All Other |  |

</details>

<details>
<summary><strong>23 — Legal</strong> (7/8 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
| ✅ | 23-1011.00 | Lawyers | [`lawyer-contracts`](./roles/lawyer-contracts/SKILL.md) |
| ✅ | 23-1012.00 | Judicial Law Clerks | [`judicial-law-clerk`](./roles/judicial-law-clerk/SKILL.md) |
| ✅ | 23-1021.00 | Administrative Law Judges, Adjudicators, and Hearing Officers | [`administrative-law-judge`](./roles/administrative-law-judge/SKILL.md) |
| ✅ | 23-1022.00 | Arbitrators, Mediators, and Conciliators | [`mediator`](./roles/mediator/SKILL.md) |
| ✅ | 23-1023.00 | Judges, Magistrate Judges, and Magistrates | [`judge`](./roles/judge/SKILL.md) |
| ✅ | 23-2011.00 | Paralegals and Legal Assistants | [`paralegal`](./roles/paralegal/SKILL.md) |
| ✅ | 23-2093.00 | Title Examiners, Abstractors, and Searchers | [`title-examiner`](./roles/title-examiner/SKILL.md) |
|  | 23-2099.00 | Legal Support Workers, All Other |  |

</details>

<details>
<summary><strong>25 — Educational Instruction and Library</strong> (1/68 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
|  | 25-1011.00 | Business Teachers, Postsecondary |  |
|  | 25-1021.00 | Computer Science Teachers, Postsecondary |  |
|  | 25-1022.00 | Mathematical Science Teachers, Postsecondary |  |
|  | 25-1031.00 | Architecture Teachers, Postsecondary |  |
|  | 25-1032.00 | Engineering Teachers, Postsecondary |  |
|  | 25-1041.00 | Agricultural Sciences Teachers, Postsecondary |  |
|  | 25-1042.00 | Biological Science Teachers, Postsecondary |  |
|  | 25-1043.00 | Forestry and Conservation Science Teachers, Postsecondary |  |
|  | 25-1051.00 | Atmospheric, Earth, Marine, and Space Sciences Teachers, Postsecondary |  |
|  | 25-1052.00 | Chemistry Teachers, Postsecondary |  |
|  | 25-1053.00 | Environmental Science Teachers, Postsecondary |  |
|  | 25-1054.00 | Physics Teachers, Postsecondary |  |
|  | 25-1061.00 | Anthropology and Archeology Teachers, Postsecondary |  |
|  | 25-1062.00 | Area, Ethnic, and Cultural Studies Teachers, Postsecondary |  |
|  | 25-1063.00 | Economics Teachers, Postsecondary |  |
|  | 25-1064.00 | Geography Teachers, Postsecondary |  |
|  | 25-1065.00 | Political Science Teachers, Postsecondary |  |
|  | 25-1066.00 | Psychology Teachers, Postsecondary |  |
|  | 25-1067.00 | Sociology Teachers, Postsecondary |  |
|  | 25-1069.00 | Social Sciences Teachers, Postsecondary, All Other |  |
|  | 25-1071.00 | Health Specialties Teachers, Postsecondary |  |
|  | 25-1072.00 | Nursing Instructors and Teachers, Postsecondary |  |
|  | 25-1081.00 | Education Teachers, Postsecondary |  |
|  | 25-1082.00 | Library Science Teachers, Postsecondary |  |
|  | 25-1111.00 | Criminal Justice and Law Enforcement Teachers, Postsecondary |  |
|  | 25-1112.00 | Law Teachers, Postsecondary |  |
|  | 25-1113.00 | Social Work Teachers, Postsecondary |  |
|  | 25-1121.00 | Art, Drama, and Music Teachers, Postsecondary |  |
|  | 25-1122.00 | Communications Teachers, Postsecondary |  |
|  | 25-1123.00 | English Language and Literature Teachers, Postsecondary |  |
|  | 25-1124.00 | Foreign Language and Literature Teachers, Postsecondary |  |
|  | 25-1125.00 | History Teachers, Postsecondary |  |
|  | 25-1126.00 | Philosophy and Religion Teachers, Postsecondary |  |
|  | 25-1192.00 | Family and Consumer Sciences Teachers, Postsecondary |  |
|  | 25-1193.00 | Recreation and Fitness Studies Teachers, Postsecondary |  |
|  | 25-1194.00 | Career/Technical Education Teachers, Postsecondary |  |
|  | 25-1199.00 | Postsecondary Teachers, All Other |  |
|  | 25-2011.00 | Preschool Teachers, Except Special Education |  |
|  | 25-2012.00 | Kindergarten Teachers, Except Special Education |  |
|  | 25-2021.00 | Elementary School Teachers, Except Special Education |  |
|  | 25-2022.00 | Middle School Teachers, Except Special and Career/Technical Education |  |
|  | 25-2023.00 | Career/Technical Education Teachers, Middle School |  |
| ✅ | 25-2031.00 | Secondary School Teachers, Except Special and Career/Technical Education | [`high-school-teacher`](./roles/high-school-teacher/SKILL.md) |
|  | 25-2032.00 | Career/Technical Education Teachers, Secondary School |  |
|  | 25-2051.00 | Special Education Teachers, Preschool |  |
|  | 25-2055.00 | Special Education Teachers, Kindergarten |  |
|  | 25-2056.00 | Special Education Teachers, Elementary School |  |
|  | 25-2057.00 | Special Education Teachers, Middle School |  |
|  | 25-2058.00 | Special Education Teachers, Secondary School |  |
|  | 25-2059.00 | Special Education Teachers, All Other |  |
|  | 25-2059.01 | Adapted Physical Education Specialists |  |
|  | 25-3011.00 | Adult Basic Education, Adult Secondary Education, and English as a Second Language Instructors |  |
|  | 25-3021.00 | Self-Enrichment Teachers |  |
|  | 25-3031.00 | Substitute Teachers, Short-Term |  |
|  | 25-3041.00 | Tutors |  |
|  | 25-3099.00 | Teachers and Instructors, All Other |  |
|  | 25-4011.00 | Archivists |  |
|  | 25-4012.00 | Curators |  |
|  | 25-4013.00 | Museum Technicians and Conservators |  |
|  | 25-4022.00 | Librarians and Media Collections Specialists |  |
|  | 25-4031.00 | Library Technicians |  |
|  | 25-9021.00 | Farm and Home Management Educators |  |
|  | 25-9031.00 | Instructional Coordinators |  |
|  | 25-9042.00 | Teaching Assistants, Preschool, Elementary, Middle, and Secondary School, Except Special Education |  |
|  | 25-9043.00 | Teaching Assistants, Special Education |  |
|  | 25-9044.00 | Teaching Assistants, Postsecondary |  |
|  | 25-9049.00 | Teaching Assistants, All Other |  |
|  | 25-9099.00 | Educational Instruction and Library Workers, All Other |  |

</details>

<details>
<summary><strong>27 — Arts, Design, Entertainment, Sports, and Media</strong> (1/45 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
|  | 27-1011.00 | Art Directors |  |
|  | 27-1012.00 | Craft Artists |  |
|  | 27-1013.00 | Fine Artists, Including Painters, Sculptors, and Illustrators |  |
|  | 27-1014.00 | Special Effects Artists and Animators |  |
|  | 27-1019.00 | Artists and Related Workers, All Other |  |
|  | 27-1021.00 | Commercial and Industrial Designers |  |
|  | 27-1022.00 | Fashion Designers |  |
|  | 27-1023.00 | Floral Designers |  |
| ✅ | 27-1024.00 | Graphic Designers | [`graphic-designer`](./roles/graphic-designer/SKILL.md) |
|  | 27-1025.00 | Interior Designers |  |
|  | 27-1026.00 | Merchandise Displayers and Window Trimmers |  |
|  | 27-1027.00 | Set and Exhibit Designers |  |
|  | 27-1029.00 | Designers, All Other |  |
|  | 27-2011.00 | Actors |  |
|  | 27-2012.00 | Producers and Directors |  |
|  | 27-2012.03 | Media Programming Directors |  |
|  | 27-2012.04 | Talent Directors |  |
|  | 27-2012.05 | Media Technical Directors/Managers |  |
|  | 27-2021.00 | Athletes and Sports Competitors |  |
|  | 27-2022.00 | Coaches and Scouts |  |
|  | 27-2023.00 | Umpires, Referees, and Other Sports Officials |  |
|  | 27-2031.00 | Dancers |  |
|  | 27-2032.00 | Choreographers |  |
|  | 27-2041.00 | Music Directors and Composers |  |
|  | 27-2042.00 | Musicians and Singers |  |
|  | 27-2091.00 | Disc Jockeys, Except Radio |  |
|  | 27-2099.00 | Entertainers and Performers, Sports and Related Workers, All Other |  |
|  | 27-3011.00 | Broadcast Announcers and Radio Disc Jockeys |  |
|  | 27-3023.00 | News Analysts, Reporters, and Journalists |  |
|  | 27-3031.00 | Public Relations Specialists |  |
|  | 27-3041.00 | Editors |  |
|  | 27-3042.00 | Technical Writers |  |
|  | 27-3043.00 | Writers and Authors |  |
|  | 27-3043.05 | Poets, Lyricists and Creative Writers |  |
|  | 27-3091.00 | Interpreters and Translators |  |
|  | 27-3092.00 | Court Reporters and Simultaneous Captioners |  |
|  | 27-3099.00 | Media and Communication Workers, All Other |  |
|  | 27-4011.00 | Audio and Video Technicians |  |
|  | 27-4012.00 | Broadcast Technicians |  |
|  | 27-4014.00 | Sound Engineering Technicians |  |
|  | 27-4015.00 | Lighting Technicians |  |
|  | 27-4021.00 | Photographers |  |
|  | 27-4031.00 | Camera Operators, Television, Video, and Film |  |
|  | 27-4032.00 | Film and Video Editors |  |
|  | 27-4099.00 | Media and Communication Equipment Workers, All Other |  |

</details>

<details>
<summary><strong>29 — Healthcare Practitioners and Technical</strong> (3/96 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
|  | 29-1011.00 | Chiropractors |  |
|  | 29-1021.00 | Dentists, General |  |
|  | 29-1022.00 | Oral and Maxillofacial Surgeons |  |
|  | 29-1023.00 | Orthodontists |  |
|  | 29-1024.00 | Prosthodontists |  |
|  | 29-1029.00 | Dentists, All Other Specialists |  |
|  | 29-1031.00 | Dietitians and Nutritionists |  |
|  | 29-1041.00 | Optometrists |  |
|  | 29-1051.00 | Pharmacists |  |
|  | 29-1071.00 | Physician Assistants |  |
|  | 29-1071.01 | Anesthesiologist Assistants |  |
|  | 29-1081.00 | Podiatrists |  |
|  | 29-1122.00 | Occupational Therapists |  |
|  | 29-1122.01 | Low Vision Therapists, Orientation and Mobility Specialists, and Vision Rehabilitation Therapists |  |
|  | 29-1123.00 | Physical Therapists |  |
|  | 29-1124.00 | Radiation Therapists |  |
|  | 29-1125.00 | Recreational Therapists |  |
|  | 29-1126.00 | Respiratory Therapists |  |
|  | 29-1127.00 | Speech-Language Pathologists |  |
|  | 29-1128.00 | Exercise Physiologists |  |
|  | 29-1129.00 | Therapists, All Other |  |
|  | 29-1129.01 | Art Therapists |  |
|  | 29-1129.02 | Music Therapists |  |
|  | 29-1131.00 | Veterinarians |  |
| ✅ | 29-1141.00 | Registered Nurses | [`registered-nurse`](./roles/registered-nurse/SKILL.md) |
|  | 29-1141.01 | Acute Care Nurses |  |
|  | 29-1141.02 | Advanced Practice Psychiatric Nurses |  |
|  | 29-1141.03 | Critical Care Nurses |  |
|  | 29-1141.04 | Clinical Nurse Specialists |  |
|  | 29-1151.00 | Nurse Anesthetists |  |
|  | 29-1161.00 | Nurse Midwives |  |
|  | 29-1171.00 | Nurse Practitioners |  |
|  | 29-1181.00 | Audiologists |  |
|  | 29-1211.00 | Anesthesiologists |  |
|  | 29-1212.00 | Cardiologists |  |
|  | 29-1213.00 | Dermatologists |  |
|  | 29-1214.00 | Emergency Medicine Physicians |  |
|  | 29-1215.00 | Family Medicine Physicians |  |
| ♻️ | 29-1216.00 | General Internal Medicine Physicians | [`physician-clinical-reasoning`](./roles/physician-clinical-reasoning/SKILL.md) |
|  | 29-1217.00 | Neurologists |  |
|  | 29-1218.00 | Obstetricians and Gynecologists |  |
|  | 29-1221.00 | Pediatricians, General |  |
|  | 29-1222.00 | Physicians, Pathologists |  |
|  | 29-1223.00 | Psychiatrists |  |
|  | 29-1224.00 | Radiologists |  |
|  | 29-1229.00 | Physicians, All Other |  |
|  | 29-1229.01 | Allergists and Immunologists |  |
|  | 29-1229.02 | Hospitalists |  |
|  | 29-1229.03 | Urologists |  |
|  | 29-1229.04 | Physical Medicine and Rehabilitation Physicians |  |
|  | 29-1229.05 | Preventive Medicine Physicians |  |
|  | 29-1229.06 | Sports Medicine Physicians |  |
|  | 29-1241.00 | Ophthalmologists, Except Pediatric |  |
|  | 29-1242.00 | Orthopedic Surgeons, Except Pediatric |  |
|  | 29-1243.00 | Pediatric Surgeons |  |
|  | 29-1249.00 | Surgeons, All Other |  |
|  | 29-1291.00 | Acupuncturists |  |
|  | 29-1292.00 | Dental Hygienists |  |
|  | 29-1299.00 | Healthcare Diagnosing or Treating Practitioners, All Other |  |
|  | 29-1299.01 | Naturopathic Physicians |  |
|  | 29-1299.02 | Orthoptists |  |
|  | 29-2011.00 | Medical and Clinical Laboratory Technologists |  |
|  | 29-2011.01 | Cytogenetic Technologists |  |
|  | 29-2011.02 | Cytotechnologists |  |
|  | 29-2011.04 | Histotechnologists |  |
|  | 29-2012.00 | Medical and Clinical Laboratory Technicians |  |
|  | 29-2012.01 | Histology Technicians |  |
|  | 29-2031.00 | Cardiovascular Technologists and Technicians |  |
|  | 29-2032.00 | Diagnostic Medical Sonographers |  |
|  | 29-2033.00 | Nuclear Medicine Technologists |  |
|  | 29-2034.00 | Radiologic Technologists and Technicians |  |
|  | 29-2035.00 | Magnetic Resonance Imaging Technologists |  |
|  | 29-2036.00 | Medical Dosimetrists |  |
|  | 29-2042.00 | Emergency Medical Technicians |  |
| ✅ | 29-2043.00 | Paramedics | [`paramedic`](./roles/paramedic/SKILL.md) |
|  | 29-2051.00 | Dietetic Technicians |  |
|  | 29-2052.00 | Pharmacy Technicians |  |
|  | 29-2053.00 | Psychiatric Technicians |  |
|  | 29-2055.00 | Surgical Technologists |  |
|  | 29-2056.00 | Veterinary Technologists and Technicians |  |
|  | 29-2057.00 | Ophthalmic Medical Technicians |  |
|  | 29-2061.00 | Licensed Practical and Licensed Vocational Nurses |  |
|  | 29-2072.00 | Medical Records Specialists |  |
|  | 29-2081.00 | Opticians, Dispensing |  |
|  | 29-2091.00 | Orthotists and Prosthetists |  |
|  | 29-2092.00 | Hearing Aid Specialists |  |
|  | 29-2099.00 | Health Technologists and Technicians, All Other |  |
|  | 29-2099.01 | Neurodiagnostic Technologists |  |
|  | 29-2099.05 | Ophthalmic Medical Technologists |  |
|  | 29-2099.08 | Patient Representatives |  |
|  | 29-9021.00 | Health Information Technologists and Medical Registrars |  |
|  | 29-9091.00 | Athletic Trainers |  |
|  | 29-9092.00 | Genetic Counselors |  |
|  | 29-9093.00 | Surgical Assistants |  |
|  | 29-9099.00 | Healthcare Practitioners and Technical Workers, All Other |  |
|  | 29-9099.01 | Midwives |  |

</details>

<details>
<summary><strong>31 — Healthcare Support</strong> (0/20 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
|  | 31-1121.00 | Home Health Aides |  |
|  | 31-1122.00 | Personal Care Aides |  |
|  | 31-1131.00 | Nursing Assistants |  |
|  | 31-1132.00 | Orderlies |  |
|  | 31-1133.00 | Psychiatric Aides |  |
|  | 31-2011.00 | Occupational Therapy Assistants |  |
|  | 31-2012.00 | Occupational Therapy Aides |  |
|  | 31-2021.00 | Physical Therapist Assistants |  |
|  | 31-2022.00 | Physical Therapist Aides |  |
|  | 31-9011.00 | Massage Therapists |  |
|  | 31-9091.00 | Dental Assistants |  |
|  | 31-9092.00 | Medical Assistants |  |
|  | 31-9093.00 | Medical Equipment Preparers |  |
|  | 31-9094.00 | Medical Transcriptionists |  |
|  | 31-9095.00 | Pharmacy Aides |  |
|  | 31-9096.00 | Veterinary Assistants and Laboratory Animal Caretakers |  |
|  | 31-9097.00 | Phlebotomists |  |
|  | 31-9099.00 | Healthcare Support Workers, All Other |  |
|  | 31-9099.01 | Speech-Language Pathology Assistants |  |
|  | 31-9099.02 | Endoscopy Technicians |  |

</details>

<details>
<summary><strong>33 — Protective Service</strong> (2/28 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
|  | 33-1011.00 | First-Line Supervisors of Correctional Officers |  |
|  | 33-1012.00 | First-Line Supervisors of Police and Detectives |  |
|  | 33-1021.00 | First-Line Supervisors of Firefighting and Prevention Workers |  |
|  | 33-1091.00 | First-Line Supervisors of Security Workers |  |
|  | 33-1099.00 | First-Line Supervisors of Protective Service Workers, All Other |  |
| ✅ | 33-2011.00 | Firefighters | [`firefighter`](./roles/firefighter/SKILL.md) |
|  | 33-2021.00 | Fire Inspectors and Investigators |  |
|  | 33-2022.00 | Forest Fire Inspectors and Prevention Specialists |  |
|  | 33-3011.00 | Bailiffs |  |
|  | 33-3012.00 | Correctional Officers and Jailers |  |
|  | 33-3021.00 | Detectives and Criminal Investigators |  |
|  | 33-3021.02 | Police Identification and Records Officers |  |
|  | 33-3021.06 | Intelligence Analysts |  |
|  | 33-3031.00 | Fish and Game Wardens |  |
|  | 33-3041.00 | Parking Enforcement Workers |  |
| ✅ | 33-3051.00 | Police and Sheriff's Patrol Officers | [`police-patrol-officer`](./roles/police-patrol-officer/SKILL.md) |
|  | 33-3051.04 | Customs and Border Protection Officers |  |
|  | 33-3052.00 | Transit and Railroad Police |  |
|  | 33-9011.00 | Animal Control Workers |  |
|  | 33-9021.00 | Private Detectives and Investigators |  |
|  | 33-9031.00 | Gambling Surveillance Officers and Gambling Investigators |  |
|  | 33-9032.00 | Security Guards |  |
|  | 33-9091.00 | Crossing Guards and Flaggers |  |
|  | 33-9092.00 | Lifeguards, Ski Patrol, and Other Recreational Protective Service Workers |  |
|  | 33-9093.00 | Transportation Security Screeners |  |
|  | 33-9094.00 | School Bus Monitors |  |
|  | 33-9099.00 | Protective Service Workers, All Other |  |
|  | 33-9099.02 | Retail Loss Prevention Specialists |  |

</details>

<details>
<summary><strong>35 — Food Preparation and Serving Related</strong> (0/18 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
|  | 35-1011.00 | Chefs and Head Cooks |  |
|  | 35-1012.00 | First-Line Supervisors of Food Preparation and Serving Workers |  |
|  | 35-2011.00 | Cooks, Fast Food |  |
|  | 35-2012.00 | Cooks, Institution and Cafeteria |  |
|  | 35-2013.00 | Cooks, Private Household |  |
|  | 35-2014.00 | Cooks, Restaurant |  |
|  | 35-2015.00 | Cooks, Short Order |  |
|  | 35-2019.00 | Cooks, All Other |  |
|  | 35-2021.00 | Food Preparation Workers |  |
|  | 35-3011.00 | Bartenders |  |
|  | 35-3023.00 | Fast Food and Counter Workers |  |
|  | 35-3023.01 | Baristas |  |
|  | 35-3031.00 | Waiters and Waitresses |  |
|  | 35-3041.00 | Food Servers, Nonrestaurant |  |
|  | 35-9011.00 | Dining Room and Cafeteria Attendants and Bartender Helpers |  |
|  | 35-9021.00 | Dishwashers |  |
|  | 35-9031.00 | Hosts and Hostesses, Restaurant, Lounge, and Coffee Shop |  |
|  | 35-9099.00 | Food Preparation and Serving Related Workers, All Other |  |

</details>

<details>
<summary><strong>37 — Building and Grounds Cleaning and Maintenance</strong> (0/10 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
|  | 37-1011.00 | First-Line Supervisors of Housekeeping and Janitorial Workers |  |
|  | 37-1012.00 | First-Line Supervisors of Landscaping, Lawn Service, and Groundskeeping Workers |  |
|  | 37-2011.00 | Janitors and Cleaners, Except Maids and Housekeeping Cleaners |  |
|  | 37-2012.00 | Maids and Housekeeping Cleaners |  |
|  | 37-2019.00 | Building Cleaning Workers, All Other |  |
|  | 37-2021.00 | Pest Control Workers |  |
|  | 37-3011.00 | Landscaping and Groundskeeping Workers |  |
|  | 37-3012.00 | Pesticide Handlers, Sprayers, and Applicators, Vegetation |  |
|  | 37-3013.00 | Tree Trimmers and Pruners |  |
|  | 37-3019.00 | Grounds Maintenance Workers, All Other |  |

</details>

<details>
<summary><strong>39 — Personal Care and Service</strong> (0/34 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
|  | 39-1013.00 | First-Line Supervisors of Gambling Services Workers |  |
|  | 39-1014.00 | First-Line Supervisors of Entertainment and Recreation Workers, Except Gambling Services |  |
|  | 39-1022.00 | First-Line Supervisors of Personal Service Workers |  |
|  | 39-2011.00 | Animal Trainers |  |
|  | 39-2021.00 | Animal Caretakers |  |
|  | 39-3011.00 | Gambling Dealers |  |
|  | 39-3012.00 | Gambling and Sports Book Writers and Runners |  |
|  | 39-3019.00 | Gambling Service Workers, All Other |  |
|  | 39-3021.00 | Motion Picture Projectionists |  |
|  | 39-3031.00 | Ushers, Lobby Attendants, and Ticket Takers |  |
|  | 39-3091.00 | Amusement and Recreation Attendants |  |
|  | 39-3092.00 | Costume Attendants |  |
|  | 39-3093.00 | Locker Room, Coatroom, and Dressing Room Attendants |  |
|  | 39-3099.00 | Entertainment Attendants and Related Workers, All Other |  |
|  | 39-4011.00 | Embalmers |  |
|  | 39-4012.00 | Crematory Operators |  |
|  | 39-4021.00 | Funeral Attendants |  |
|  | 39-4031.00 | Morticians, Undertakers, and Funeral Arrangers |  |
|  | 39-5011.00 | Barbers |  |
|  | 39-5012.00 | Hairdressers, Hairstylists, and Cosmetologists |  |
|  | 39-5091.00 | Makeup Artists, Theatrical and Performance |  |
|  | 39-5092.00 | Manicurists and Pedicurists |  |
|  | 39-5093.00 | Shampooers |  |
|  | 39-5094.00 | Skincare Specialists |  |
|  | 39-6011.00 | Baggage Porters and Bellhops |  |
|  | 39-6012.00 | Concierges |  |
|  | 39-7011.00 | Tour Guides and Escorts |  |
|  | 39-7012.00 | Travel Guides |  |
|  | 39-9011.00 | Childcare Workers |  |
|  | 39-9011.01 | Nannies |  |
|  | 39-9031.00 | Exercise Trainers and Group Fitness Instructors |  |
|  | 39-9032.00 | Recreation Workers |  |
|  | 39-9041.00 | Residential Advisors |  |
|  | 39-9099.00 | Personal Care and Service Workers, All Other |  |

</details>

<details>
<summary><strong>41 — Sales and Related</strong> (3/23 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
|  | 41-1011.00 | First-Line Supervisors of Retail Sales Workers |  |
|  | 41-1012.00 | First-Line Supervisors of Non-Retail Sales Workers |  |
|  | 41-2011.00 | Cashiers |  |
|  | 41-2012.00 | Gambling Change Persons and Booth Cashiers |  |
|  | 41-2021.00 | Counter and Rental Clerks |  |
|  | 41-2022.00 | Parts Salespersons |  |
|  | 41-2031.00 | Retail Salespersons |  |
|  | 41-3011.00 | Advertising Sales Agents |  |
|  | 41-3021.00 | Insurance Sales Agents |  |
|  | 41-3031.00 | Securities, Commodities, and Financial Services Sales Agents |  |
|  | 41-3041.00 | Travel Agents |  |
|  | 41-3091.00 | Sales Representatives of Services, Except Advertising, Insurance, Financial Services, and Travel |  |
| ♻️ | 41-4011.00 | Sales Representatives, Wholesale and Manufacturing, Technical and Scientific Products | [`sales-account-executive`](./roles/sales-account-executive/SKILL.md) |
|  | 41-4011.07 | Solar Sales Representatives and Assessors |  |
|  | 41-4012.00 | Sales Representatives, Wholesale and Manufacturing, Except Technical and Scientific Products |  |
|  | 41-9011.00 | Demonstrators and Product Promoters |  |
|  | 41-9012.00 | Models |  |
| ✅ | 41-9021.00 | Real Estate Brokers | [`real-estate-broker`](./roles/real-estate-broker/SKILL.md) |
|  | 41-9022.00 | Real Estate Sales Agents |  |
| ✅ | 41-9031.00 | Sales Engineers | [`sales-engineer`](./roles/sales-engineer/SKILL.md) |
|  | 41-9041.00 | Telemarketers |  |
|  | 41-9091.00 | Door-to-Door Sales Workers, News and Street Vendors, and Related Workers |  |
|  | 41-9099.00 | Sales and Related Workers, All Other |  |

</details>

<details>
<summary><strong>43 — Office and Administrative Support</strong> (1/55 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
|  | 43-1011.00 | First-Line Supervisors of Office and Administrative Support Workers |  |
|  | 43-2011.00 | Switchboard Operators, Including Answering Service |  |
|  | 43-2021.00 | Telephone Operators |  |
|  | 43-2099.00 | Communications Equipment Operators, All Other |  |
|  | 43-3011.00 | Bill and Account Collectors |  |
|  | 43-3021.00 | Billing and Posting Clerks |  |
| ✅ | 43-3031.00 | Bookkeeping, Accounting, and Auditing Clerks | [`bookkeeping-accounting-clerk`](./roles/bookkeeping-accounting-clerk/SKILL.md) |
|  | 43-3041.00 | Gambling Cage Workers |  |
|  | 43-3051.00 | Payroll and Timekeeping Clerks |  |
|  | 43-3061.00 | Procurement Clerks |  |
|  | 43-3071.00 | Tellers |  |
|  | 43-3099.00 | Financial Clerks, All Other |  |
|  | 43-4011.00 | Brokerage Clerks |  |
|  | 43-4021.00 | Correspondence Clerks |  |
|  | 43-4031.00 | Court, Municipal, and License Clerks |  |
|  | 43-4041.00 | Credit Authorizers, Checkers, and Clerks |  |
|  | 43-4051.00 | Customer Service Representatives |  |
|  | 43-4061.00 | Eligibility Interviewers, Government Programs |  |
|  | 43-4071.00 | File Clerks |  |
|  | 43-4081.00 | Hotel, Motel, and Resort Desk Clerks |  |
|  | 43-4111.00 | Interviewers, Except Eligibility and Loan |  |
|  | 43-4121.00 | Library Assistants, Clerical |  |
|  | 43-4131.00 | Loan Interviewers and Clerks |  |
|  | 43-4141.00 | New Accounts Clerks |  |
|  | 43-4151.00 | Order Clerks |  |
|  | 43-4161.00 | Human Resources Assistants, Except Payroll and Timekeeping |  |
|  | 43-4171.00 | Receptionists and Information Clerks |  |
|  | 43-4181.00 | Reservation and Transportation Ticket Agents and Travel Clerks |  |
|  | 43-4199.00 | Information and Record Clerks, All Other |  |
|  | 43-5011.00 | Cargo and Freight Agents |  |
|  | 43-5011.01 | Freight Forwarders |  |
|  | 43-5021.00 | Couriers and Messengers |  |
|  | 43-5031.00 | Public Safety Telecommunicators |  |
|  | 43-5032.00 | Dispatchers, Except Police, Fire, and Ambulance |  |
|  | 43-5041.00 | Meter Readers, Utilities |  |
|  | 43-5051.00 | Postal Service Clerks |  |
|  | 43-5052.00 | Postal Service Mail Carriers |  |
|  | 43-5053.00 | Postal Service Mail Sorters, Processors, and Processing Machine Operators |  |
|  | 43-5061.00 | Production, Planning, and Expediting Clerks |  |
|  | 43-5071.00 | Shipping, Receiving, and Inventory Clerks |  |
|  | 43-5111.00 | Weighers, Measurers, Checkers, and Samplers, Recordkeeping |  |
|  | 43-6011.00 | Executive Secretaries and Executive Administrative Assistants |  |
|  | 43-6012.00 | Legal Secretaries and Administrative Assistants |  |
|  | 43-6013.00 | Medical Secretaries and Administrative Assistants |  |
|  | 43-6014.00 | Secretaries and Administrative Assistants, Except Legal, Medical, and Executive |  |
|  | 43-9021.00 | Data Entry Keyers |  |
|  | 43-9022.00 | Word Processors and Typists |  |
|  | 43-9031.00 | Desktop Publishers |  |
|  | 43-9041.00 | Insurance Claims and Policy Processing Clerks |  |
|  | 43-9051.00 | Mail Clerks and Mail Machine Operators, Except Postal Service |  |
|  | 43-9061.00 | Office Clerks, General |  |
|  | 43-9071.00 | Office Machine Operators, Except Computer |  |
|  | 43-9081.00 | Proofreaders and Copy Markers |  |
|  | 43-9111.00 | Statistical Assistants |  |
|  | 43-9199.00 | Office and Administrative Support Workers, All Other |  |

</details>

<details>
<summary><strong>45 — Farming, Fishing, and Forestry</strong> (0/14 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
|  | 45-1011.00 | First-Line Supervisors of Farming, Fishing, and Forestry Workers |  |
|  | 45-2011.00 | Agricultural Inspectors |  |
|  | 45-2021.00 | Animal Breeders |  |
|  | 45-2041.00 | Graders and Sorters, Agricultural Products |  |
|  | 45-2091.00 | Agricultural Equipment Operators |  |
|  | 45-2092.00 | Farmworkers and Laborers, Crop, Nursery, and Greenhouse |  |
|  | 45-2093.00 | Farmworkers, Farm, Ranch, and Aquacultural Animals |  |
|  | 45-2099.00 | Agricultural Workers, All Other |  |
|  | 45-3031.00 | Fishing and Hunting Workers |  |
|  | 45-4011.00 | Forest and Conservation Workers |  |
|  | 45-4021.00 | Fallers |  |
|  | 45-4022.00 | Logging Equipment Operators |  |
|  | 45-4023.00 | Log Graders and Scalers |  |
|  | 45-4029.00 | Logging Workers, All Other |  |

</details>

<details>
<summary><strong>47 — Construction and Extraction</strong> (1/65 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
|  | 47-1011.00 | First-Line Supervisors of Construction Trades and Extraction Workers |  |
|  | 47-1011.03 | Solar Energy Installation Managers |  |
|  | 47-2011.00 | Boilermakers |  |
|  | 47-2021.00 | Brickmasons and Blockmasons |  |
|  | 47-2022.00 | Stonemasons |  |
|  | 47-2031.00 | Carpenters |  |
|  | 47-2041.00 | Carpet Installers |  |
|  | 47-2042.00 | Floor Layers, Except Carpet, Wood, and Hard Tiles |  |
|  | 47-2043.00 | Floor Sanders and Finishers |  |
|  | 47-2044.00 | Tile and Stone Setters |  |
|  | 47-2051.00 | Cement Masons and Concrete Finishers |  |
|  | 47-2053.00 | Terrazzo Workers and Finishers |  |
|  | 47-2061.00 | Construction Laborers |  |
|  | 47-2071.00 | Paving, Surfacing, and Tamping Equipment Operators |  |
|  | 47-2072.00 | Pile Driver Operators |  |
|  | 47-2073.00 | Operating Engineers and Other Construction Equipment Operators |  |
|  | 47-2081.00 | Drywall and Ceiling Tile Installers |  |
|  | 47-2082.00 | Tapers |  |
| ✅ | 47-2111.00 | Electricians | [`electrician`](./roles/electrician/SKILL.md) |
|  | 47-2121.00 | Glaziers |  |
|  | 47-2131.00 | Insulation Workers, Floor, Ceiling, and Wall |  |
|  | 47-2132.00 | Insulation Workers, Mechanical |  |
|  | 47-2141.00 | Painters, Construction and Maintenance |  |
|  | 47-2142.00 | Paperhangers |  |
|  | 47-2151.00 | Pipelayers |  |
|  | 47-2152.00 | Plumbers, Pipefitters, and Steamfitters |  |
|  | 47-2152.04 | Solar Thermal Installers and Technicians |  |
|  | 47-2161.00 | Plasterers and Stucco Masons |  |
|  | 47-2171.00 | Reinforcing Iron and Rebar Workers |  |
|  | 47-2181.00 | Roofers |  |
|  | 47-2211.00 | Sheet Metal Workers |  |
|  | 47-2221.00 | Structural Iron and Steel Workers |  |
|  | 47-2231.00 | Solar Photovoltaic Installers |  |
|  | 47-3011.00 | Helpers--Brickmasons, Blockmasons, Stonemasons, and Tile and Marble Setters |  |
|  | 47-3012.00 | Helpers--Carpenters |  |
|  | 47-3013.00 | Helpers--Electricians |  |
|  | 47-3014.00 | Helpers--Painters, Paperhangers, Plasterers, and Stucco Masons |  |
|  | 47-3015.00 | Helpers--Pipelayers, Plumbers, Pipefitters, and Steamfitters |  |
|  | 47-3016.00 | Helpers--Roofers |  |
|  | 47-3019.00 | Helpers, Construction Trades, All Other |  |
|  | 47-4011.00 | Construction and Building Inspectors |  |
|  | 47-4011.01 | Energy Auditors |  |
|  | 47-4021.00 | Elevator and Escalator Installers and Repairers |  |
|  | 47-4031.00 | Fence Erectors |  |
|  | 47-4041.00 | Hazardous Materials Removal Workers |  |
|  | 47-4051.00 | Highway Maintenance Workers |  |
|  | 47-4061.00 | Rail-Track Laying and Maintenance Equipment Operators |  |
|  | 47-4071.00 | Septic Tank Servicers and Sewer Pipe Cleaners |  |
|  | 47-4091.00 | Segmental Pavers |  |
|  | 47-4099.00 | Construction and Related Workers, All Other |  |
|  | 47-4099.03 | Weatherization Installers and Technicians |  |
|  | 47-5011.00 | Derrick Operators, Oil and Gas |  |
|  | 47-5012.00 | Rotary Drill Operators, Oil and Gas |  |
|  | 47-5013.00 | Service Unit Operators, Oil and Gas |  |
|  | 47-5022.00 | Excavating and Loading Machine and Dragline Operators, Surface Mining |  |
|  | 47-5023.00 | Earth Drillers, Except Oil and Gas |  |
|  | 47-5032.00 | Explosives Workers, Ordnance Handling Experts, and Blasters |  |
|  | 47-5041.00 | Continuous Mining Machine Operators |  |
|  | 47-5043.00 | Roof Bolters, Mining |  |
|  | 47-5044.00 | Loading and Moving Machine Operators, Underground Mining |  |
|  | 47-5049.00 | Underground Mining Machine Operators, All Other |  |
|  | 47-5051.00 | Rock Splitters, Quarry |  |
|  | 47-5071.00 | Roustabouts, Oil and Gas |  |
|  | 47-5081.00 | Helpers--Extraction Workers |  |
|  | 47-5099.00 | Extraction Workers, All Other |  |

</details>

<details>
<summary><strong>49 — Installation, Maintenance, and Repair</strong> (0/52 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
|  | 49-1011.00 | First-Line Supervisors of Mechanics, Installers, and Repairers |  |
|  | 49-2011.00 | Computer, Automated Teller, and Office Machine Repairers |  |
|  | 49-2021.00 | Radio, Cellular, and Tower Equipment Installers and Repairers |  |
|  | 49-2022.00 | Telecommunications Equipment Installers and Repairers, Except Line Installers |  |
|  | 49-2091.00 | Avionics Technicians |  |
|  | 49-2092.00 | Electric Motor, Power Tool, and Related Repairers |  |
|  | 49-2093.00 | Electrical and Electronics Installers and Repairers, Transportation Equipment |  |
|  | 49-2094.00 | Electrical and Electronics Repairers, Commercial and Industrial Equipment |  |
|  | 49-2095.00 | Electrical and Electronics Repairers, Powerhouse, Substation, and Relay |  |
|  | 49-2096.00 | Electronic Equipment Installers and Repairers, Motor Vehicles |  |
|  | 49-2097.00 | Audiovisual Equipment Installers and Repairers |  |
|  | 49-2098.00 | Security and Fire Alarm Systems Installers |  |
|  | 49-3011.00 | Aircraft Mechanics and Service Technicians |  |
|  | 49-3021.00 | Automotive Body and Related Repairers |  |
|  | 49-3022.00 | Automotive Glass Installers and Repairers |  |
|  | 49-3023.00 | Automotive Service Technicians and Mechanics |  |
|  | 49-3031.00 | Bus and Truck Mechanics and Diesel Engine Specialists |  |
|  | 49-3041.00 | Farm Equipment Mechanics and Service Technicians |  |
|  | 49-3042.00 | Mobile Heavy Equipment Mechanics, Except Engines |  |
|  | 49-3043.00 | Rail Car Repairers |  |
|  | 49-3051.00 | Motorboat Mechanics and Service Technicians |  |
|  | 49-3052.00 | Motorcycle Mechanics |  |
|  | 49-3053.00 | Outdoor Power Equipment and Other Small Engine Mechanics |  |
|  | 49-3091.00 | Bicycle Repairers |  |
|  | 49-3092.00 | Recreational Vehicle Service Technicians |  |
|  | 49-3093.00 | Tire Repairers and Changers |  |
|  | 49-9011.00 | Mechanical Door Repairers |  |
|  | 49-9012.00 | Control and Valve Installers and Repairers, Except Mechanical Door |  |
|  | 49-9021.00 | Heating, Air Conditioning, and Refrigeration Mechanics and Installers |  |
|  | 49-9031.00 | Home Appliance Repairers |  |
|  | 49-9041.00 | Industrial Machinery Mechanics |  |
|  | 49-9043.00 | Maintenance Workers, Machinery |  |
|  | 49-9044.00 | Millwrights |  |
|  | 49-9045.00 | Refractory Materials Repairers, Except Brickmasons |  |
|  | 49-9051.00 | Electrical Power-Line Installers and Repairers |  |
|  | 49-9052.00 | Telecommunications Line Installers and Repairers |  |
|  | 49-9061.00 | Camera and Photographic Equipment Repairers |  |
|  | 49-9062.00 | Medical Equipment Repairers |  |
|  | 49-9063.00 | Musical Instrument Repairers and Tuners |  |
|  | 49-9064.00 | Watch and Clock Repairers |  |
|  | 49-9069.00 | Precision Instrument and Equipment Repairers, All Other |  |
|  | 49-9071.00 | Maintenance and Repair Workers, General |  |
|  | 49-9081.00 | Wind Turbine Service Technicians |  |
|  | 49-9091.00 | Coin, Vending, and Amusement Machine Servicers and Repairers |  |
|  | 49-9092.00 | Commercial Divers |  |
|  | 49-9094.00 | Locksmiths and Safe Repairers |  |
|  | 49-9095.00 | Manufactured Building and Mobile Home Installers |  |
|  | 49-9096.00 | Riggers |  |
|  | 49-9097.00 | Signal and Track Switch Repairers |  |
|  | 49-9098.00 | Helpers--Installation, Maintenance, and Repair Workers |  |
|  | 49-9099.00 | Installation, Maintenance, and Repair Workers, All Other |  |
|  | 49-9099.01 | Geothermal Technicians |  |

</details>

<details>
<summary><strong>51 — Production</strong> (0/114 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
|  | 51-1011.00 | First-Line Supervisors of Production and Operating Workers |  |
|  | 51-2011.00 | Aircraft Structure, Surfaces, Rigging, and Systems Assemblers |  |
|  | 51-2021.00 | Coil Winders, Tapers, and Finishers |  |
|  | 51-2022.00 | Electrical and Electronic Equipment Assemblers |  |
|  | 51-2023.00 | Electromechanical Equipment Assemblers |  |
|  | 51-2031.00 | Engine and Other Machine Assemblers |  |
|  | 51-2041.00 | Structural Metal Fabricators and Fitters |  |
|  | 51-2051.00 | Fiberglass Laminators and Fabricators |  |
|  | 51-2061.00 | Timing Device Assemblers and Adjusters |  |
|  | 51-2092.00 | Team Assemblers |  |
|  | 51-2099.00 | Assemblers and Fabricators, All Other |  |
|  | 51-3011.00 | Bakers |  |
|  | 51-3021.00 | Butchers and Meat Cutters |  |
|  | 51-3022.00 | Meat, Poultry, and Fish Cutters and Trimmers |  |
|  | 51-3023.00 | Slaughterers and Meat Packers |  |
|  | 51-3091.00 | Food and Tobacco Roasting, Baking, and Drying Machine Operators and Tenders |  |
|  | 51-3092.00 | Food Batchmakers |  |
|  | 51-3093.00 | Food Cooking Machine Operators and Tenders |  |
|  | 51-3099.00 | Food Processing Workers, All Other |  |
|  | 51-4021.00 | Extruding and Drawing Machine Setters, Operators, and Tenders, Metal and Plastic |  |
|  | 51-4022.00 | Forging Machine Setters, Operators, and Tenders, Metal and Plastic |  |
|  | 51-4023.00 | Rolling Machine Setters, Operators, and Tenders, Metal and Plastic |  |
|  | 51-4031.00 | Cutting, Punching, and Press Machine Setters, Operators, and Tenders, Metal and Plastic |  |
|  | 51-4032.00 | Drilling and Boring Machine Tool Setters, Operators, and Tenders, Metal and Plastic |  |
|  | 51-4033.00 | Grinding, Lapping, Polishing, and Buffing Machine Tool Setters, Operators, and Tenders, Metal and Plastic |  |
|  | 51-4034.00 | Lathe and Turning Machine Tool Setters, Operators, and Tenders, Metal and Plastic |  |
|  | 51-4035.00 | Milling and Planing Machine Setters, Operators, and Tenders, Metal and Plastic |  |
|  | 51-4041.00 | Machinists |  |
|  | 51-4051.00 | Metal-Refining Furnace Operators and Tenders |  |
|  | 51-4052.00 | Pourers and Casters, Metal |  |
|  | 51-4061.00 | Model Makers, Metal and Plastic |  |
|  | 51-4062.00 | Patternmakers, Metal and Plastic |  |
|  | 51-4071.00 | Foundry Mold and Coremakers |  |
|  | 51-4072.00 | Molding, Coremaking, and Casting Machine Setters, Operators, and Tenders, Metal and Plastic |  |
|  | 51-4081.00 | Multiple Machine Tool Setters, Operators, and Tenders, Metal and Plastic |  |
|  | 51-4111.00 | Tool and Die Makers |  |
|  | 51-4121.00 | Welders, Cutters, Solderers, and Brazers |  |
|  | 51-4122.00 | Welding, Soldering, and Brazing Machine Setters, Operators, and Tenders |  |
|  | 51-4191.00 | Heat Treating Equipment Setters, Operators, and Tenders, Metal and Plastic |  |
|  | 51-4192.00 | Layout Workers, Metal and Plastic |  |
|  | 51-4193.00 | Plating Machine Setters, Operators, and Tenders, Metal and Plastic |  |
|  | 51-4194.00 | Tool Grinders, Filers, and Sharpeners |  |
|  | 51-4199.00 | Metal Workers and Plastic Workers, All Other |  |
|  | 51-5111.00 | Prepress Technicians and Workers |  |
|  | 51-5112.00 | Printing Press Operators |  |
|  | 51-5113.00 | Print Binding and Finishing Workers |  |
|  | 51-6011.00 | Laundry and Dry-Cleaning Workers |  |
|  | 51-6021.00 | Pressers, Textile, Garment, and Related Materials |  |
|  | 51-6031.00 | Sewing Machine Operators |  |
|  | 51-6041.00 | Shoe and Leather Workers and Repairers |  |
|  | 51-6042.00 | Shoe Machine Operators and Tenders |  |
|  | 51-6051.00 | Sewers, Hand |  |
|  | 51-6052.00 | Tailors, Dressmakers, and Custom Sewers |  |
|  | 51-6061.00 | Textile Bleaching and Dyeing Machine Operators and Tenders |  |
|  | 51-6062.00 | Textile Cutting Machine Setters, Operators, and Tenders |  |
|  | 51-6063.00 | Textile Knitting and Weaving Machine Setters, Operators, and Tenders |  |
|  | 51-6064.00 | Textile Winding, Twisting, and Drawing Out Machine Setters, Operators, and Tenders |  |
|  | 51-6091.00 | Extruding and Forming Machine Setters, Operators, and Tenders, Synthetic and Glass Fibers |  |
|  | 51-6092.00 | Fabric and Apparel Patternmakers |  |
|  | 51-6093.00 | Upholsterers |  |
|  | 51-6099.00 | Textile, Apparel, and Furnishings Workers, All Other |  |
|  | 51-7011.00 | Cabinetmakers and Bench Carpenters |  |
|  | 51-7021.00 | Furniture Finishers |  |
|  | 51-7031.00 | Model Makers, Wood |  |
|  | 51-7032.00 | Patternmakers, Wood |  |
|  | 51-7041.00 | Sawing Machine Setters, Operators, and Tenders, Wood |  |
|  | 51-7042.00 | Woodworking Machine Setters, Operators, and Tenders, Except Sawing |  |
|  | 51-7099.00 | Woodworkers, All Other |  |
|  | 51-8011.00 | Nuclear Power Reactor Operators |  |
|  | 51-8012.00 | Power Distributors and Dispatchers |  |
|  | 51-8013.00 | Power Plant Operators |  |
|  | 51-8013.03 | Biomass Plant Technicians |  |
|  | 51-8013.04 | Hydroelectric Plant Technicians |  |
|  | 51-8021.00 | Stationary Engineers and Boiler Operators |  |
|  | 51-8031.00 | Water and Wastewater Treatment Plant and System Operators |  |
|  | 51-8091.00 | Chemical Plant and System Operators |  |
|  | 51-8092.00 | Gas Plant Operators |  |
|  | 51-8093.00 | Petroleum Pump System Operators, Refinery Operators, and Gaugers |  |
|  | 51-8099.00 | Plant and System Operators, All Other |  |
|  | 51-8099.01 | Biofuels Processing Technicians |  |
|  | 51-9011.00 | Chemical Equipment Operators and Tenders |  |
|  | 51-9012.00 | Separating, Filtering, Clarifying, Precipitating, and Still Machine Setters, Operators, and Tenders |  |
|  | 51-9021.00 | Crushing, Grinding, and Polishing Machine Setters, Operators, and Tenders |  |
|  | 51-9022.00 | Grinding and Polishing Workers, Hand |  |
|  | 51-9023.00 | Mixing and Blending Machine Setters, Operators, and Tenders |  |
|  | 51-9031.00 | Cutters and Trimmers, Hand |  |
|  | 51-9032.00 | Cutting and Slicing Machine Setters, Operators, and Tenders |  |
|  | 51-9041.00 | Extruding, Forming, Pressing, and Compacting Machine Setters, Operators, and Tenders |  |
|  | 51-9051.00 | Furnace, Kiln, Oven, Drier, and Kettle Operators and Tenders |  |
|  | 51-9061.00 | Inspectors, Testers, Sorters, Samplers, and Weighers |  |
|  | 51-9071.00 | Jewelers and Precious Stone and Metal Workers |  |
|  | 51-9071.06 | Gem and Diamond Workers |  |
|  | 51-9081.00 | Dental Laboratory Technicians |  |
|  | 51-9082.00 | Medical Appliance Technicians |  |
|  | 51-9083.00 | Ophthalmic Laboratory Technicians |  |
|  | 51-9111.00 | Packaging and Filling Machine Operators and Tenders |  |
|  | 51-9123.00 | Painting, Coating, and Decorating Workers |  |
|  | 51-9124.00 | Coating, Painting, and Spraying Machine Setters, Operators, and Tenders |  |
|  | 51-9141.00 | Semiconductor Processing Technicians |  |
|  | 51-9151.00 | Photographic Process Workers and Processing Machine Operators |  |
|  | 51-9161.00 | Computer Numerically Controlled Tool Operators |  |
|  | 51-9162.00 | Computer Numerically Controlled Tool Programmers |  |
|  | 51-9191.00 | Adhesive Bonding Machine Operators and Tenders |  |
|  | 51-9192.00 | Cleaning, Washing, and Metal Pickling Equipment Operators and Tenders |  |
|  | 51-9193.00 | Cooling and Freezing Equipment Operators and Tenders |  |
|  | 51-9194.00 | Etchers and Engravers |  |
|  | 51-9195.00 | Molders, Shapers, and Casters, Except Metal and Plastic |  |
|  | 51-9195.03 | Stone Cutters and Carvers, Manufacturing |  |
|  | 51-9195.04 | Glass Blowers, Molders, Benders, and Finishers |  |
|  | 51-9195.05 | Potters, Manufacturing |  |
|  | 51-9196.00 | Paper Goods Machine Setters, Operators, and Tenders |  |
|  | 51-9197.00 | Tire Builders |  |
|  | 51-9198.00 | Helpers--Production Workers |  |
|  | 51-9199.00 | Production Workers, All Other |  |

</details>

<details>
<summary><strong>53 — Transportation and Material Moving</strong> (0/57 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
|  | 53-1041.00 | Aircraft Cargo Handling Supervisors |  |
|  | 53-1042.00 | First-Line Supervisors of Helpers, Laborers, and Material Movers, Hand |  |
|  | 53-1042.01 | Recycling Coordinators |  |
|  | 53-1043.00 | First-Line Supervisors of Material-Moving Machine and Vehicle Operators |  |
|  | 53-1044.00 | First-Line Supervisors of Passenger Attendants |  |
|  | 53-1049.00 | First-Line Supervisors of Transportation Workers, All Other |  |
|  | 53-2011.00 | Airline Pilots, Copilots, and Flight Engineers |  |
|  | 53-2012.00 | Commercial Pilots |  |
|  | 53-2021.00 | Air Traffic Controllers |  |
|  | 53-2022.00 | Airfield Operations Specialists |  |
|  | 53-2031.00 | Flight Attendants |  |
|  | 53-3011.00 | Ambulance Drivers and Attendants, Except Emergency Medical Technicians |  |
|  | 53-3031.00 | Driver/Sales Workers |  |
|  | 53-3032.00 | Heavy and Tractor-Trailer Truck Drivers |  |
|  | 53-3033.00 | Light Truck Drivers |  |
|  | 53-3051.00 | Bus Drivers, School |  |
|  | 53-3052.00 | Bus Drivers, Transit and Intercity |  |
|  | 53-3053.00 | Shuttle Drivers and Chauffeurs |  |
|  | 53-3054.00 | Taxi Drivers |  |
|  | 53-3099.00 | Motor Vehicle Operators, All Other |  |
|  | 53-4011.00 | Locomotive Engineers |  |
|  | 53-4013.00 | Rail Yard Engineers, Dinkey Operators, and Hostlers |  |
|  | 53-4022.00 | Railroad Brake, Signal, and Switch Operators and Locomotive Firers |  |
|  | 53-4031.00 | Railroad Conductors and Yardmasters |  |
|  | 53-4041.00 | Subway and Streetcar Operators |  |
|  | 53-4099.00 | Rail Transportation Workers, All Other |  |
|  | 53-5011.00 | Sailors and Marine Oilers |  |
|  | 53-5021.00 | Captains, Mates, and Pilots of Water Vessels |  |
|  | 53-5022.00 | Motorboat Operators |  |
|  | 53-5031.00 | Ship Engineers |  |
|  | 53-6011.00 | Bridge and Lock Tenders |  |
|  | 53-6021.00 | Parking Attendants |  |
|  | 53-6031.00 | Automotive and Watercraft Service Attendants |  |
|  | 53-6032.00 | Aircraft Service Attendants |  |
|  | 53-6041.00 | Traffic Technicians |  |
|  | 53-6051.00 | Transportation Inspectors |  |
|  | 53-6051.01 | Aviation Inspectors |  |
|  | 53-6051.07 | Transportation Vehicle, Equipment and Systems Inspectors, Except Aviation |  |
|  | 53-6061.00 | Passenger Attendants |  |
|  | 53-6099.00 | Transportation Workers, All Other |  |
|  | 53-7011.00 | Conveyor Operators and Tenders |  |
|  | 53-7021.00 | Crane and Tower Operators |  |
|  | 53-7031.00 | Dredge Operators |  |
|  | 53-7041.00 | Hoist and Winch Operators |  |
|  | 53-7051.00 | Industrial Truck and Tractor Operators |  |
|  | 53-7061.00 | Cleaners of Vehicles and Equipment |  |
|  | 53-7062.00 | Laborers and Freight, Stock, and Material Movers, Hand |  |
|  | 53-7062.04 | Recycling and Reclamation Workers |  |
|  | 53-7063.00 | Machine Feeders and Offbearers |  |
|  | 53-7064.00 | Packers and Packagers, Hand |  |
|  | 53-7065.00 | Stockers and Order Fillers |  |
|  | 53-7071.00 | Gas Compressor and Gas Pumping Station Operators |  |
|  | 53-7072.00 | Pump Operators, Except Wellhead Pumpers |  |
|  | 53-7073.00 | Wellhead Pumpers |  |
|  | 53-7081.00 | Refuse and Recyclable Material Collectors |  |
|  | 53-7121.00 | Tank Car, Truck, and Ship Loaders |  |
|  | 53-7199.00 | Material Moving Workers, All Other |  |

</details>

<details>
<summary><strong>55 — Military Specific</strong> (0/19 drafted)</summary>

| Status | O*NET-SOC Code | Occupation | Repo role |
|---|---|---|---|
|  | 55-1011.00 | Air Crew Officers |  |
|  | 55-1012.00 | Aircraft Launch and Recovery Officers |  |
|  | 55-1013.00 | Armored Assault Vehicle Officers |  |
|  | 55-1014.00 | Artillery and Missile Officers |  |
|  | 55-1015.00 | Command and Control Center Officers |  |
|  | 55-1016.00 | Infantry Officers |  |
|  | 55-1017.00 | Special Forces Officers |  |
|  | 55-1019.00 | Military Officer Special and Tactical Operations Leaders, All Other |  |
|  | 55-2011.00 | First-Line Supervisors of Air Crew Members |  |
|  | 55-2012.00 | First-Line Supervisors of Weapons Specialists/Crew Members |  |
|  | 55-2013.00 | First-Line Supervisors of All Other Tactical Operations Specialists |  |
|  | 55-3011.00 | Air Crew Members |  |
|  | 55-3012.00 | Aircraft Launch and Recovery Specialists |  |
|  | 55-3013.00 | Armored Assault Vehicle Crew Members |  |
|  | 55-3014.00 | Artillery and Missile Crew Members |  |
|  | 55-3015.00 | Command and Control Center Specialists |  |
|  | 55-3016.00 | Infantry |  |
|  | 55-3018.00 | Special Forces |  |
|  | 55-3019.00 | Military Enlisted Tactical Operations and Air/Weapons Specialists and Crew Members, All Other |  |

</details>

<!-- CHECKLIST END -->

## Spec-2 upgrade queue

Roles drafted before the current spec — they lack the `references/` trio (deep-dive, `red-flags.md`, `vocabulary.md`) and the spec-2 SKILL.md structure. This queue is the standing TODO for upgrade sessions: pick the top unclaimed entry and follow the "Exact recipe for upgrading a legacy role to spec 2" in [CONTRIBUTING.md](./CONTRIBUTING.md). A role drops off this list automatically once its frontmatter says `spec: 2` and this script is re-run.

**42 roles awaiting upgrade:**

| Repo role | Category |
|---|---|
| [`accountant-controller`](./roles/accountant-controller/SKILL.md) | finance |
| [`administrative-services-manager`](./roles/administrative-services-manager/SKILL.md) | operations |
| [`advertising-promotions-manager`](./roles/advertising-promotions-manager/SKILL.md) | marketing |
| [`agricultural-manager`](./roles/agricultural-manager/SKILL.md) | operations |
| [`biofuels-production-manager`](./roles/biofuels-production-manager/SKILL.md) | operations |
| [`biomass-power-plant-manager`](./roles/biomass-power-plant-manager/SKILL.md) | operations |
| [`chief-executive`](./roles/chief-executive/SKILL.md) | operations |
| [`chief-sustainability-officer`](./roles/chief-sustainability-officer/SKILL.md) | operations |
| [`compensation-benefits-manager`](./roles/compensation-benefits-manager/SKILL.md) | operations |
| [`computer-information-systems-manager`](./roles/computer-information-systems-manager/SKILL.md) | engineering |
| [`construction-manager`](./roles/construction-manager/SKILL.md) | operations |
| [`customer-success-manager`](./roles/customer-success-manager/SKILL.md) | sales |
| [`devops-sre`](./roles/devops-sre/SKILL.md) | engineering |
| [`education-administrator-k12`](./roles/education-administrator-k12/SKILL.md) | operations |
| [`education-administrator-other`](./roles/education-administrator-other/SKILL.md) | operations |
| [`education-administrator-postsecondary`](./roles/education-administrator-postsecondary/SKILL.md) | operations |
| [`education-childcare-administrator-preschool`](./roles/education-childcare-administrator-preschool/SKILL.md) | operations |
| [`facilities-manager`](./roles/facilities-manager/SKILL.md) | operations |
| [`financial-analyst`](./roles/financial-analyst/SKILL.md) | finance |
| [`fundraising-manager`](./roles/fundraising-manager/SKILL.md) | operations |
| [`general-operations-manager`](./roles/general-operations-manager/SKILL.md) | operations |
| [`geothermal-production-manager`](./roles/geothermal-production-manager/SKILL.md) | operations |
| [`hr-people-manager`](./roles/hr-people-manager/SKILL.md) | operations |
| [`hydroelectric-production-manager`](./roles/hydroelectric-production-manager/SKILL.md) | operations |
| [`industrial-production-manager`](./roles/industrial-production-manager/SKILL.md) | operations |
| [`investment-fund-manager`](./roles/investment-fund-manager/SKILL.md) | finance |
| [`legislator`](./roles/legislator/SKILL.md) | operations |
| [`marketing-manager`](./roles/marketing-manager/SKILL.md) | marketing |
| [`physician-clinical-reasoning`](./roles/physician-clinical-reasoning/SKILL.md) | healthcare |
| [`public-relations-manager`](./roles/public-relations-manager/SKILL.md) | marketing |
| [`purchasing-manager`](./roles/purchasing-manager/SKILL.md) | operations |
| [`quality-control-systems-manager`](./roles/quality-control-systems-manager/SKILL.md) | operations |
| [`sales-account-executive`](./roles/sales-account-executive/SKILL.md) | sales |
| [`sales-manager`](./roles/sales-manager/SKILL.md) | sales |
| [`security-manager`](./roles/security-manager/SKILL.md) | operations |
| [`software-engineer`](./roles/software-engineer/SKILL.md) | engineering |
| [`supply-chain-manager`](./roles/supply-chain-manager/SKILL.md) | operations |
| [`technical-recruiter`](./roles/technical-recruiter/SKILL.md) | operations |
| [`training-development-manager`](./roles/training-development-manager/SKILL.md) | operations |
| [`transportation-storage-distribution-manager`](./roles/transportation-storage-distribution-manager/SKILL.md) | operations |
| [`treasurer-controller`](./roles/treasurer-controller/SKILL.md) | finance |
| [`ux-designer`](./roles/ux-designer/SKILL.md) | design |

## Roles outside this list

Some roles already in this repo don't map cleanly to a single O*NET occupation — either because O*NET's granularity is coarser (a whole occupation covers what industry practice splits into several distinct roles) or because the role is a newer specialization O*NET hasn't caught up to yet:

| Repo role | Why it's not mapped |
|---|---|
| [`customer-success-manager`](./roles/customer-success-manager/SKILL.md) | A SaaS-era role that doesn't fit the closest O*NET candidates (`43-4051.00` Customer Service Representatives is too junior/generic). |
| [`data-engineer`](./roles/data-engineer/SKILL.md) | No distinct O*NET occupation for general pipeline/ETL data engineering; closest candidates (`15-1243.00` Database Architects, taken by `database-architect`, and `15-1243.01` Data Warehousing Specialists, which is BI/warehouse-specific) don't capture the role. |
| [`devops-sre`](./roles/devops-sre/SKILL.md) | Site Reliability Engineering is a post-O*NET-taxonomy specialization within `15-1244.00`/`15-1241.00`-type titles; no distinct SOC code exists. |
| [`embedded-firmware-engineer`](./roles/embedded-firmware-engineer/SKILL.md) | No distinct O*NET occupation for embedded/firmware software engineering; `17-2072.00` Electronics Engineers, Except Computer explicitly excludes computer-related work, and `15-1252.00` Software Developers (taken by `software-engineer`) doesn't capture the hardware-interfacing specifics. |
| [`frontend-engineer`](./roles/frontend-engineer/SKILL.md) | No distinct O*NET occupation for frontend performance/accessibility engineering; folds into `15-1254.00` Web Developers (already used by `full-stack-developer`) or `15-1252.00` Software Developers (already used by `software-engineer`). |
| [`ml-engineer`](./roles/ml-engineer/SKILL.md) | No distinct O*NET occupation for ML/AI engineering; folds into `15-2051.00` Data Scientists (already used by `data-scientist`) or `15-1252.00` Software Developers (already used by `software-engineer`) depending on taxonomy version. |
| [`mobile-engineer`](./roles/mobile-engineer/SKILL.md) | No distinct O*NET occupation for mobile app engineering; folds into `15-1252.00` Software Developers (already used by `software-engineer`). |
| [`platform-engineer`](./roles/platform-engineer/SKILL.md) | Platform engineering is a post-O*NET-taxonomy specialization, same 15-1244.00/15-1241.00-adjacent territory as devops-sre; no distinct SOC code exists. |
| [`product-manager`](./roles/product-manager/SKILL.md) | No distinct O*NET occupation for tech/software product management; closest broad match (`11-3021.00` Computer and Information Systems Managers) doesn't capture the role well enough to link. |
| [`technical-recruiter`](./roles/technical-recruiter/SKILL.md) | Falls inside the broader `13-1071.00` Human Resources Specialists occupation rather than having its own code. |

## Beyond O*NET

O*NET is US-centric and skews toward formal, salaried employment. For international coverage or informal/entrepreneurial roles it doesn't capture well, consider cross-referencing the ILO's [ISCO](https://ilostat.ilo.org/resources/concepts-and-definitions/classification-occupation/) or the EU's [ESCO](https://esco.ec.europa.eu/en) taxonomies when proposing a new role in a PR.

## Requested but missing

Queries the CLI's `match` command couldn't confidently resolve, logged to `data/gap-log.jsonl` and ranked by frequency here. A query that keeps recurring under one parent role's shadow — e.g. a narrow niche a generic role doesn't quite cover — is the concrete signal to draft a specialization leaf.

**No unresolved queries logged yet.**

## Needs refresh

Roles flagged `status: needs-refresh` in frontmatter — a periodic re-score against AUTHORING.md's rubric came back below threshold, or a cited source went stale. Not removed from the library, just due for a revision PR.

**None currently flagged.**

## Deprecated

Roles flagged `status: deprecated` — failed re-audit repeatedly, or the niche itself went obsolete. Excluded from the counts and checklist above; files stay in the repo (moved to `roles/_deprecated/<slug>/`), nothing is deleted.

**None currently deprecated.**
