# Architecture

The campus firewall connects PR1 (`10.1.1.0/24`), PR2 (`10.2.2.0/24`), DMZ (`172.16.10.0/24`), and OUT (`203.0.113.0/24`). `configs/campus-zbpf.cfg.template` configures the interfaces, NAT, zones, ACLs, class maps, policy maps, and zone pairs.

| Source | Destination | Services |
| --- | --- | --- |
| PR1, PR2 | OUT | ICMP, HTTP, HTTPS, DNS |
| PR1, PR2 | DMZ | ICMP, web, mail, DNS |
| OUT | DMZ | ICMP, web, SMTP, DNS |
| DMZ | OUT | ICMP, SMTP, DNS |

All other new flows are dropped. Return traffic is permitted by ZBPF state inspection.

## Flood controls

`configs/dos-mitigation.cfg` applies policing to ICMP and HTTP traffic and uses a three-second TCP SYN wait time for inspected HTTP sessions. Run it only on the isolated OUTSIDE/INSIDE topology.
