AWS VPC deployed in `us-east-1` with a three-tier architecture across two availability zones.

```mermaid
flowchart TB
    Internet["Internet"]
    IGW["Internet Gateway"]
    NAT["NAT Gateway"]

    subgraph VPC["VPC"]
        subgraph Public["Public Subnets"]
            Pub1["public-az1"]
            Pub2["public-az2"]
            Bastion["Bastion Host"]
        end

        subgraph App["App Subnets"]
            App1["app-az1"]
            App2["app-az2"]
        end

        subgraph Data["Data Subnets"]
            Data1["data-az1"]
            Data2["data-az2"]
        end
    end

    Internet --> IGW
    IGW --> Pub1
    IGW --> Pub2

    Pub1 --> NAT
    NAT --> App1
    NAT --> App2

    Internet --> Bastion
    Bastion --> App1
    Bastion --> App2

    App1 --> Data1
    App1 --> Data2
    App2 --> Data1
    App2 --> Data2
```

The security configuration is as follows:
1. Public Subnets routes to 0.0.0.0/0 via Internet Gateway
2. The App subnets are private and do not have direct internet access. Only allowed inbound traffic in the security group is allowed.
3. Database subnets are also private with no internet route possible. Only allowed traffic from the app tier security group.

Web Tier allows HTTP and HTTPS traffic from anywhere, with SSH traffic restricted to a trusted IP address. The outbound traffic is unrestricted. App tier only allows application port from Web tier. Database Tier only allows DB port from App tier. The combination of using distinct subnet tiers for public, private app, and private data with routing tables, an internet gateway, and NAT gateway with least-privilege security groups and NACLs secures and controls the traffic flow between the tiers.