# Architecture Notes - Cisco ZBPF Firewall and DoS Mitigation Lab

## Lab Topology

Two GNS3 scenarios are represented: a campus segmentation topology with PR1/PR2/DMZ/OUT zones, and a two-zone OUTSIDE/INSIDE topology for ICMP and TCP SYN flood mitigation.

## Evidence Flow

Router console outputs, Nmap probes, screenshots, and Wireshark captures were reduced to report figures and text summaries. Raw captures are excluded.

## Publication Boundary

The repository keeps report source and selected reviewed evidence. It deliberately excludes:

- Cisco IOS/GNS3 appliance images
- raw PCAP files
- course PDFs and private handouts
- local GNS3 project identifiers
- temporary debug logs

## Reproduction Assumptions

The lab was executed in GNS3 using Cisco/GNS3 appliances and Linux containers. Re-running the full topology requires local access to those appliances and the original lab guide. The portable CI only validates repository hygiene.
