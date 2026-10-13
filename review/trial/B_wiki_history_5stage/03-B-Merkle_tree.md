# 3. Merkle tree

`B-Merkle_tree` · [B_wiki_history_5stage](README.md)

Source: <https://en.wikipedia.org/w/index.php?title=Merkle_tree&action=history> · License: https://creativecommons.org/licenses/by-sa/4.0/ · 475 revisions in history; 33 candidate versions sampled

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 2 | 0 | 0.00 | source_title |
| 1 | earliest_version | 433 | 0 | 0.25 | enwiki rev 21428283 (2005-08-20) |
| 2 | early_revision | 762 | 4 | 0.51 | enwiki rev 368494254 (2010-06-16) |
| 3 | late_revision | 1054 | 10 | 0.76 | enwiki rev 746533641 (2016-10-28) |
| 4 | final | 1244 | 22 | 1.00 | enwiki rev 1375083916 (2026-09-15) |

<details><summary><b>Step 0 — title</b> (2 words)</summary>

````text
Merkle tree
````

</details>

<details><summary><b>Step 1 — earliest_version</b> (433 words)</summary>

````text
Hash trees are a concept in computer programming. They are also known as Merkle Hash Trees and Tiger-tree hashes. Hash trees are an extension of the simpler concept hash list, which in turn is an extension of the old concept of hashing for instance a file.

Before you read this article we recommend you read about hash lists first.

A hash tree is a tree of hashes where the leaves in the tree are hashes of the data blocks in for instance a file or in a set of files. The main use of hash trees are to make sure that data blocks received from other peers in a p2p system are received undamaged and unaltered. And even to check that the other peers do not lie and send fake blocks. But note that hash trees can be used to protect any kind of data stored and handled in computers.

In the top of a hash tree there is a "top hash". (Or "root hash" or "master hash" if you will.) Before you download a file on a p2p network you usually get the top hash from some source you trust. For instance a friend or a web site that you by experience know usually has good recommendations of files to download. When you have the top hash you can then receive the hash tree from any non-trusted source. For instance download the hash tree from any peer in the p2p network. Then you can check the received hash tree against the top hash that you trust. If the hash tree is damaged (the other peer perhaps even tried to cheat you) you can try to download the hash tree from other peers until you get a correct hash tree.

The main difference from a hash list is that you can download just a branch of the hash tree at a time if you want to and still check the integrity of that branch even though you don't have the whole tree yet. This can be neat since often you want to split files up in very small data blocks so you only have to re-download small blocks if they get damaged. If the hashed file is very big such a hash tree or hash list becomes fairly big. So if it is a tree you can download one small branch quickly, check the integrity of the branch and then start downloading data blocks.

There are several additional tricks, benefits and details regarding hash trees, too many to describe here.

Tree hashes are used in for instance the Gnutella2 p2p file sharing protocol.
````

</details>

<details><summary><b>Step 2 — early_revision</b> (762 words)</summary>

````text
In cryptography and computer science Hash trees or Merkle trees are a type of data structure which contains a tree of summary information about a larger piece of data – for instance a file – used to verify its contents. Hash trees are an extension of hash lists, which in turn are an extension of hashing. Hash trees where the underlying hash function is Tiger are often called Tiger trees or Tiger tree hashes.

## Uses

Hash trees can be used to protect any kind of data stored, handled and transferred in and between computers. Currently the main use of hash trees is to make sure that data blocks received from other peers in a peer-to-peer network are received undamaged and unaltered, and even to check that the other peers do not lie and send fake blocks. Suggestions have been made to use hash trees in trusted computing systems. Sun Microsystems has used Hash Trees in the ZFS filesystem[1]. Hash Trees are used in Google Wave protocol [2] and in tarsnap backup system.

Hash trees were invented in 1979 by Ralph Merkle [3]. The original purpose was to make it possible to efficiently handle many Lamport one-time signatures. Lamport signatures are believed to still be secure in the event that quantum computers become reality. Unfortunately each Lamport key can only be used to sign a single message. But combined with hash trees they can be used for many messages and then become a fairly efficient digital signature scheme.

## How hash trees work

A hash tree is a tree of hashes in which the leaves are hashes of data blocks in, for instance, a file or set of files. Nodes further up in the tree are the hashes of their respective children. For example, in the picture hash 0 is the result of hashing hash 0-0 and then hash 0-1. That is, hash 0 = hash( hash 0-0 + hash 0-1 ) where + denotes concatenation.

Most hash tree implementations are binary (two child nodes under each node) but they can just as well use many more child nodes under each node.

Usually, a cryptographic hash function such as SHA-1, Whirlpool, or Tiger is used for the hashing. If the hash tree only needs to protect against unintentional damage, much less secure checksums such as CRCs can be used.

In the top of a hash tree there is a top hash (or root hash or master hash). Before downloading a file on a p2p network, in most cases the top hash is acquired from a trusted source, for instance a friend or a web site that is known to have good recommendations of files to download. When the top hash is available, the hash tree can be received from any non-trusted source, like any peer in the p2p network. Then, the received hash tree is checked against the trusted top hash, and if the hash tree is damaged or fake, another hash tree from another source will be tried until the program finds one that matches the top hash.

The main difference from a hash list is that one branch of the hash tree can be downloaded at a time and the integrity of each branch can be checked immediately, even though the whole tree is not available yet. This can be an advantage since it is efficient to split files up in very small data blocks so that only small blocks have to be redownloaded if they get damaged. If the hashed file is very big, such a hash tree or hash list becomes fairly big. But if it is a tree, one small branch can be downloaded quickly, the integrity of the branch can be checked, and then the downloading of data blocks can start.

There are several additional tricks, benefits and details regarding hash trees. See the references and external links below for more in-depth information.

## Tiger tree hash

The Tiger tree hash is probably the most widely used form of hash tree. It uses a binary hash tree (two child nodes under each node), usually has a data block size of 1024-bytes and uses the cryptographically secure Tiger hash.

Tiger tree hashes are used in the Gnutella, Gnutella2, and Direct Connect P2P file sharing protocols and in file sharing applications such as

Phex, BearShare, LimeWire, Shareaza, DC++[4] and Valknut.

References:
[1] Jeff Bonwick's Blog ZFS End-to-End Data Integrity
[2] Google Wave Federation Protocol [http://www.waveprotocol.org/whitepapers/wave-protocol-verification Wave Protocol Verification Paper]
[3] R. C. Merkle, A digital signature based on a conventional encryption function, Crypto '87
[4] "DC++'s feature list"
````

</details>

<details><summary><b>Step 3 — late_revision</b> (1054 words)</summary>

````text
In cryptography and computer science, a hash tree or Merkle tree is a tree in which every non-leaf node is labelled with the hash of the labels or values (in case of leaves) of its child nodes. Hash trees allow efficient and secure verification of the contents of large data structures. Hash trees are a generalization of hash lists and hash chains.

Demonstrating that a leaf node is a part of the given hash tree requires processing an amount of data proportional to the logarithm of the number of nodes of the tree;[1] this contrasts with hash lists, where the amount is proportional to the number of nodes.

The concept of hash trees is named after Ralph Merkle who patented it in 1979.[2,3]

## Uses

Hash trees can be used to verify any kind of data stored, handled and transferred in and between computers. Currently the main use of hash trees is to make sure that data blocks received from other peers in a peer-to-peer network are received undamaged and unaltered, and even to check that the other peers do not lie and send fake blocks. Suggestions have been made to use hash trees in trusted computing systems.[4] Hash trees are used in the IPFS, Btrfs and ZFS file systems[5] (to counter data degradation[6]), BitTorrent protocol, Apache Wave protocol,[7] Git distributed revision control system, the Tahoe-LAFS backup system, the Bitcoin peer-to-peer network, the Ethereum peer-to-peer network,[8] the Certificate Transparency framework, and a number of NoSQL systems like Apache Cassandra, Riak and DynamoDB.[9]

## Overview

A hash tree is a tree of hashes in which the leaves are hashes of data blocks in, for instance, a file or set of files. Nodes further up in the tree are the hashes of their respective children. For example, in the picture hash 0 is the result of hashing the result of concatenating hash 0-0 and hash 0-1. That is, hash 0 = hash( hash 0-0 + hash 0-1 ) where + denotes concatenation.

Most hash tree implementations are binary (two child nodes under each node) but they can just as well use many more child nodes under each node.

Usually, a cryptographic hash function such as SHA-2 is used for the hashing . If the hash tree only needs to protect against unintentional damage, much less secure checksums such as CRCs can be used.

In the top of a hash tree there is a top hash (or root hash or master hash). Before downloading a file on a p2p network, in most cases the top hash is acquired from a trusted source, for instance a friend or a web site that is known to have good recommendations of files to download. When the top hash is available, the hash tree can be received from any non-trusted source, like any peer in the p2p network. Then, the received hash tree is checked against the trusted top hash, and if the hash tree is damaged or fake, another hash tree from another source will be tried until the program finds one that matches the top hash.

The main difference from a hash list is that one branch of the hash tree can be downloaded at a time and the integrity of each branch can be checked immediately, even though the whole tree is not available yet. For example, in the picture, the integrity of data block 2 can be verified immediately if the tree already contains hash 0-0 and hash 1 by hashing the data block and iteratively combining the result with hash 0-0 and then hash 1 and finally comparing the result with the top hash. Similarly, the integrity of data block 3 can be verified if the tree already has hash 1-1 and hash 0. This can be an advantage since it is efficient to split files up in very small data blocks so that only small blocks have to be re-downloaded if they get damaged. If the hashed file is very big, such a hash tree or hash list becomes fairly big. But if it is a tree, one small branch can be downloaded quickly, the integrity of the branch can be checked, and then the downloading of data blocks can start.

### Second preimage attack

The Merkle hash root does not indicate the tree depth, enabling a second-preimage attack in which an attacker creates a document other than the original that has the same Merkle hash root. For the example above, an attacker can create a new document containing two data blocks, where the first is hash 0-0 + hash 0-1, and the second is hash 1-0 + hash 1-1.

One simple fix is defined in Certificate Transparency: when computing leaf node hashes, a 0x00 byte is prepended to the hash data, while 0x01 is prepended when computing internal node hashes. Limiting the hash tree size is a prerequisite of some formal security proofs, and helps in making some proofs tighter. Some implementations limit the tree depth using hash tree depth prefixes before hashes, so any extracted hash chain is defined to be valid only if the prefix decreases at each step and is still positive when the leaf is reached.

### Tiger tree hash

The Tiger tree hash is a widely used form of hash tree. It uses a binary hash tree (two child nodes under each node), usually has a data block size of 1024 bytes and uses the cryptographically secure Tiger hash.[10]

Tiger tree hashes are used in Gnutella, Gnutella2, and Direct Connect P2P file sharing protocols and in file sharing applications such as Phex, BearShare, LimeWire, Shareaza, DC++[11] and Valknut.

### Example

Base32: RBOEI7UYRYO5SUXGER5NMUOEZ5O6E4BHPP2MRFQ

URN: urn:tree:tiger:RBOEI7UYRYO5SUXGER5NMUOEZ5O6E4BHPP2MRFQ

magnet: magnet:?xt=urn:tree:tiger:RBOEI7UYRYO5SUXGER5NMUOEZ5O6E4BHPP2MRFQ

References:
[1] Georg Becker. (2008-07-18). Merkle Signature Schemes, Merkle Trees and Their Cryptanalysis. Ruhr-Universität Bochum. http://www.emsec.rub.de/media/crypto/attachments/files/2011/04/becker_1.pdf
[2] Merkle, R. C.. (1988). Advances in Cryptology — CRYPTO '87. doi:10.1007/3-540-48184-2_32
[3] Method of providing digital signatures.
[4] J. Kilian. Improved efﬁcient arguments (preliminary version). In CRYPTO, 1995.
[5] Jeff Bonwick's Blog ZFS End-to-End Data Integrity
[6] Likai Liu. Bitrot Resistance on a Single Drive. likai.org. http://lifecs.likai.org/2014/06/bitrot-resistance-on-single-drive.html
[7] Google Wave Federation Protocol [http://www.waveprotocol.org/protocol/whitepapers/wave-protocol-verification Wave Protocol Verification Paper]
[8] Cryptocash, cryptocurrencies, and cryptocontracts, Koblitz and Menezes, Designs, Codes and Cryptography, Volume 78, Issue 1, pp 87-102, January 2016.
[9] Adam Marcus. The NoSQL Ecosystem. aosabook.org. http://www.aosabook.org/en/nosql.html
[10] Tree Hash EXchange format (THEX) (archive)
[11] "DC++'s feature list"
````

</details>

<details><summary><b>Step 4 — final</b> (1244 words)</summary>

````text
In cryptography and computer science, a hash tree or Merkle tree is a tree in which every "leaf" node is labelled with the cryptographic hash of a data block, and every node that is not a leaf (called a branch, inner node, or inode) is labelled with the cryptographic hash of the labels of its child nodes. A hash tree allows efficient and secure verification of the contents of a large data structure. A hash tree is a generalization of a hash list and a hash chain.

Demonstrating that a leaf node is a part of a given binary hash tree requires computing a number of hashes proportional to the logarithm of the number of leaf nodes in the tree.[1] Conversely, in a hash list, the number is proportional to the number of leaf nodes itself. A Merkle tree is therefore an efficient example of a cryptographic commitment scheme, in which the root of the tree is seen as a commitment and leaf nodes may be revealed and proven to be part of the original commitment.[2]

The concept of a hash tree is named after Ralph Merkle, who patented it in 1979.[3,4]

## Uses

Hash trees can be used to verify any kind of data stored, handled and transferred in and between computers. They can help ensure that data blocks received from other peers in a peer-to-peer network are received undamaged and unaltered, and even to check that the other peers do not lie and send fake blocks.

Hash trees are used in:

hash-based cryptography.

InterPlanetary File System (IPFS),

BitTorrent

hashtree[5]

ZFS file system[6] (to counter data degradation[7]);

Dat protocol;

Apache Wave protocol;[8]

Git and Mercurial distributed revision control systems (although, strictly speaking, they use directed acyclic graphs, not trees);

the Tahoe-LAFS backup system;

Zeronet;

OpenZFS[9]

the Bitcoin and Ethereum peer-to-peer networks;[10]

the Certificate Transparency framework;

Merkle Tree Certificates;[11]

the Nix package manager and descendants like GNU Guix;[12]

a number of NoSQL systems such as Apache Cassandra, Riak, and Dynamo.[13]

Suggestions have been made to use hash trees in trusted computing systems.[14]

## Overview

A hash tree is a tree of hashes in which the leaves (i.e., leaf nodes, sometimes also called "leafs") are hashes of data blocks in, for instance, a file or set of files. Nodes farther up in the tree are the hashes of their respective children. For example, in the above picture hash 0 is the result of hashing the concatenation of hash 0-0 and hash 0-1. That is, hash 0 = hash( hash 0-0 + hash 0-1 ) where "+" denotes concatenation.

Most hash tree implementations are binary (two child nodes under each node) but they can just as well use many more child nodes under each node.

Usually, a cryptographic hash function such as SHA-2 is used for the hashing. If the hash tree only needs to protect against unintentional damage, non-cryptographic checksums such as CRCs can be used.

In the top of a hash tree there is a top hash (or root hash or master hash). Before downloading a file on a P2P network, in most cases the top hash is acquired from a trusted source, for instance a friend or a web site that is known to have good recommendations of files to download. When the top hash is available, the hash tree can be received from any non-trusted source, like any peer in the P2P network. Then, the received hash tree is checked against the trusted top hash, and if the hash tree is damaged or fake, another hash tree from another source will be tried until the program finds one that matches the top hash.[15]

The main difference from a hash list is that one branch of the hash tree can be downloaded at a time and the integrity of each branch can be checked immediately, even though the whole tree is not available yet. For example, in the picture, the integrity of data block L2 can be verified immediately if the tree already contains hash 0-0 and hash 1 by hashing the data block and iteratively combining the result with hash 0-0 and then hash 1 and finally comparing the result with the top hash. Similarly, the integrity of data block L3 can be verified if the tree already has hash 1-1 and hash 0. This can be an advantage since it is efficient to split files up in very small data blocks so that only small blocks have to be re-downloaded if they get damaged. If the hashed file is big, such a hash list or hash chain becomes fairly big. But if it is a tree, one small branch can be downloaded quickly, the integrity of the branch can be checked, and then the downloading of data blocks can start.

### Second preimage attack

The Merkle hash root does not indicate the tree depth, enabling a second-preimage attack in which an attacker creates a document other than the original that has the same Merkle hash root. For the example above, an attacker can create a new document containing two data blocks, where the first is hash 0-0 + hash 0-1, and the second is hash 1-0 + hash 1-1.[16,17]

One simple fix is defined in Certificate Transparency: when computing leaf node hashes, a 0x00 byte is prepended to the hash data, while 0x01 is prepended when computing internal node hashes.[15] Limiting the hash tree size is a prerequisite of some formal security proofs, and helps in making some proofs tighter. Some implementations limit the tree depth using hash tree depth prefixes before hashes, so any extracted hash chain is defined to be valid only if the prefix decreases at each step and is still positive when the leaf is reached.

### Tiger tree hash

The Tiger tree hash is a widely used form of hash tree. It uses a binary hash tree (two child nodes under each node), usually has a data block size of 1024 bytes and uses the Tiger hash.[18]

Tiger tree hashes are used in Gnutella,[19] Gnutella2, and Direct Connect P2P file sharing protocols[20] and in file sharing applications such as Phex,[21] BearShare, LimeWire, Shareaza, DC++[22] and gtk-gnutella.[23]

References:
[1] Becker, Georg. (2008-07-18). Merkle Signature Schemes, Merkle Trees and Their Cryptanalysis. Ruhr-Universität Bochum. http://www.emsec.rub.de/media/crypto/attachments/files/2011/04/becker_1.pdf
[2] Handbook of Applied Cryptography. cacr.uwaterloo.ca. https://cacr.uwaterloo.ca/hac/
[3] Merkle, R. C.. (1988). Advances in Cryptology – CRYPTO '87. doi:10.1007/3-540-48184-2_32
[4] Method of providing digital signatures.
[5] hashtree developer page. https://hashtree.cc/#/dev
[6] Bonwick, Jeff. (2005-12-08). ZFS End-to-End Data Integrity. blogs.oracle.com. https://blogs.oracle.com/bonwick/entry/zfs_end_to_end_data
[7] Likai Liu. Bitrot Resistance on a Single Drive. likai.org. http://lifecs.likai.org/2014/06/bitrot-resistance-on-single-drive.html
[8] General Verifiable Federation. Google Wave Protocol. http://www.waveprotocol.org/whitepapers/wave-protocol-verification
[9] Introduction to ZFS — openzfs latest documentation. openzfs.readthedocs.io. https://openzfs.readthedocs.io/en/latest/introduction.html
[10] Koblitz, Neal. (January 2016). Cryptocash, cryptocurrencies, and cryptocontracts. Designs, Codes and Cryptography. doi:10.1007/s10623-015-0148-5
[11] (2026-05-24). Merkle Tree Certificates. Internet Engineering Task Force. https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/
[12] Dolstra, E. The Purely Functional Software Deployment Model. PhD thesis, Faculty of Science, Utrecht, The Netherlands. January 2006. p.21 .
[13] Adam Marcus. The NoSQL Ecosystem. aosabook.org. http://www.aosabook.org/en/nosql.html
[14] Kilian, J.. (1995). Advances in Cryptology — CRYPT0' 95. doi:10.1007/3-540-44750-4_25
[15] Laurie, B.. (June 2013). Certificate Transparency. IETF. doi:10.17487/rfc6962
[16] (January 2009). Selected Areas in Cryptography. SAC. doi:10.1007/978-3-642-05445-7_25
[17] (2008). Advances in Cryptology – EUROCRYPT 2008. doi:10.1007/978-3-540-78967-3_16
[18] Chapweske, J.. (March 4, 2003). Tree Hash EXchange format (THEX). http://open-content.net/specs/draft-jchapweske-thex-02.html
[19] tigertree.c File Reference. Gtk-Gnutella. https://gtk-gnutella.sourceforge.net/doxygen/tigertree_8c.html
[20] Audit: P2P DirectConnect Application. Symantec. https://www.symantec.com/security_response/attacksignatures/detail.jsp?asid=21587
[21] (7 Jan 2007). Phex 3.0.0 released. Phex. http://www.phex.org/mambo/content/view/80/2/
[22] DC++'s feature list. dcplusplus.sourceforge.net. http://dcplusplus.sourceforge.net/features.html
[23] Development. GTK-Gnutella. http://gtk-gnutella.sourceforge.net/en/?page=devel
````

</details>
