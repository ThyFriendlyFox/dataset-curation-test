# 1. Python PEP: Sample reStructuredText PEP Template

`C-pep_pep-0012` · [full/C_github_commits_9step](README.md)

Source: <https://github.com/python/peps/blob/545c670f1e986162eb7161d63c944108e504bd09/peps/pep-0012.rst> · License: Public domain / CC0-1.0 (PEP text) · 58 commits touching the file; 50 distinct versions

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 4 | 0 | 0.00 | source_title |
| 1 | revision_1 | 3233 | 8 | 0.64 | commit 9ca8e6bba0 (2002-08-26) |
| 2 | revision_2 | 3418 | 7 | 0.70 | commit cd1e507dd8 (2021-12-06) |
| 3 | revision_3 | 3371 | 4 | 0.73 | commit 52ffaebe9b (2022-02-02) |
| 4 | revision_4 | 3517 | 1 | 0.81 | commit 8e33abd30f (2022-02-17) |
| 5 | revision_5 | 3481 | 1 | 0.86 | commit e3a44f348f (2022-03-04) |
| 6 | revision_6 | 3604 | 0 | 0.91 | commit 4370f8f737 (2022-03-23) |
| 7 | revision_7 | 3888 | 0 | 0.96 | commit f87de8284c (2022-08-02) |
| 8 | final | 3994 | 0 | 1.00 | commit 76b2b6a2ab (2026-03-04) |

<details><summary><b>Step 0 — title</b> (4 words)</summary>

````text
Sample reStructuredText PEP Template
````

</details>

<details><summary><b>Step 1 — revision_1</b> (3233 words)</summary>

````text
Abstract
========

This PEP provides a boilerplate or sample template for creating your
own reStructuredText PEPs.  In conjunction with the content guidelines
in PEP 1 [1]_, this should make it easy for you to conform your own
PEPs to the format outlined below.

Note: if you are reading this PEP via the web, you should first grab
the text (reStructuredText) version in order to complete the steps
below.  **DO NOT USE THE HTML FILE AS YOUR TEMPLATE!**

To get the text version of this file, look at the top of the page and
click on the link titled "PEP Source".

If you would prefer not to use markup in your PEP, please see PEP 9,
"Sample Plaintext PEP Template" [2]_.


Rationale
=========

PEP submissions come in a wide variety of forms, not all adhering
to the format guidelines set forth below.  Use this template, in
conjunction with the format guidelines below, to ensure that your
PEP submission won't get automatically rejected because of form.

ReStructuredText is offered as an alternative to plaintext PEPs, to
allow PEP authors more functionality and expressivity, while
maintaining easy readability in the source text.  The processed HTML
form makes the functionality accessible to readers: live hyperlinks,
styled text, tables, images, and automatic tables of contents, among
other advantages.  For an example of a PEP marked up with
reStructuredText, see PEP 287.


How to Use This Template
========================

To use this template you must first decide whether your PEP is going
to be Informational or Standards Track.  Most PEPs are Standards Track
because they propose a new feature for the Python language or standard
library.  When in doubt, read PEP 1 for details.

Once you've decided which type of PEP yours is going to be, follow the
directions below.

- Make a copy of this file (``.txt`` file, **not** HTML!) and perform
  the following edits.

- Replace the "PEP: 9" header with "PEP: XXX" since you don't yet have
  a PEP number assignment.

- Change the Title header to the title of your PEP.

- Leave the Version and Last-Modified headers alone; we'll take care
  of those when we check your PEP into CVS.

- Change the Author header to include your name, and optionally your
  email address.  Be sure to follow the format carefully: your name
  must appear first, and it must not be contained in parentheses.
  Your email address may appear second (it can also be omitted) and if
  it appears, it must appear in angle brackets.

- If there is a mailing list for discussion of your new feature, add a
  Discussions-To header right after the Author header.  You should not
  add a Discussions-To header if the mailing list to be used is either
  python-list@python.org or python-dev@python.org, or if discussions
  should be sent to you directly.  Most Informational PEPs don't have
  a Discussions-To header.

- Change the Status header to "Draft".

- For Standards Track PEPs, change the Type header to "Standards
  Track".

- For Informational PEPs, change the Type header to "Informational".

- For Standards Track PEPs, if your feature depends on the acceptance
  of some other currently in-development PEP, add a Requires header
  right after the Type header.  The value should be the PEP number of
  the PEP yours depends on.  Don't add this header if your dependent
  feature is described in a Final PEP.

- Change the Created header to today's date.  Be sure to follow the
  format carefully: it must be in ``dd-mmm-yyyy`` format, where the
  ``mmm`` is the 3 English letter month abbreviation, i.e. one of Jan,
  Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec.

- For Standards Track PEPs, after the Created header, add a
  Python-Version header and set the value to the next planned version
  of Python, i.e. the one your new feature will hopefully make its
  first appearance in.  Do not use an alpha or beta release
  designation here.  Thus, if the last version of Python was 2.2 alpha
  1 and you're hoping to get your new feature into Python 2.2, set the
  header to::

      Python-Version: 2.2

- Leave Post-History alone for now; you'll add dates to this header
  each time you post your PEP to python-list@python.org or
  python-dev@python.org.  If you posted your PEP to the lists on
  August 14, 2001 and September 3, 2001, the Post-History header would
  look like::

      Post-History: 14-Aug-2001, 03-Sept-2001

  You must manually add new dates and check them in.  If you don't
  have check-in privileges, send your changes to the PEP editor.

- Add a Replaces header if your PEP obsoletes an earlier PEP.  The
  value of this header is the number of the PEP that your new PEP is
  replacing.  Only add this header if the older PEP is in "final"
  form, i.e. is either Accepted, Final, or Rejected.  You aren't
  replacing an older open PEP if you're submitting a competing idea.

- Now write your Abstract, Rationale, and other content for your PEP,
  replacing all this gobbledygook with your own text. Be sure to
  adhere to the format guidelines below, specifically on the
  prohibition of tab characters and the indentation requirements.

- Update your References and Copyright section.  Usually you'll place
  your PEP into the public domain, in which case just leave the
  Copyright section alone.  Alternatively, you can use the `Open
  Publication License`__, but public domain is still strongly
  preferred.

  __ http://www.opencontent.org/openpub/

- Leave the Emacs stanza at the end of this file alone, including the
  formfeed character ("^L", or ``\f``).

- Send your PEP submission to the PEP editor, Barry Warsaw, at
  peps@python.org.


ReStructuredText PEP Formatting Requirements
============================================

The following is a PEP-specific summary of reStructuredText syntax.
For the sake of simplicity and brevity, much detail is omitted.  For
more detail, see `Resources`_ below.  `Literal blocks`_ (in which no
markup processing is done) are used for examples throughout, to
illustrate the plaintext markup.


General
-------

You must adhere to the Emacs convention of adding two spaces at the
end of every sentence.  You should fill your paragraphs to column 70,
but under no circumstances should your lines extend past column 79.
If your code samples spill over column 79, you should rewrite them.

Tab characters must never appear in the document at all.  A PEP should
include the standard Emacs stanza included by example at the bottom of
this PEP.


Section Headings
----------------

PEP headings must begin in column zero and the initial letter of each
word must be capitalized as in book titles.  Acronyms should be in all
capitals.  Section titles must be adorned with an underline, a single
repeated punctuation character, which begins in column zero and must
extend at least as far as the right edge of the title text (4
characters minimum).  First-level section titles are underlined with
"=" (equals signs), second-level section titles with "-" (hyphens),
and third-level section titles with "'" (single quotes or
apostrophes).  For example::

    First-Level Title
    =================

    Second-Level Title
    ------------------

    Third-Level Title
    '''''''''''''''''

If there are more than three levels of sections in your PEP, you may
insert overline/underline-adorned titles for the first and second
levels as follows::

    ============================
    First-Level Title (optional)
    ============================

    -----------------------------
    Second-Level Title (optional)
    -----------------------------

    Third-Level Title
    =================

    Fourth-Level Title
    ------------------

    Fifth-Level Title
    '''''''''''''''''

You shouldn't have more than five levels of sections in your PEP.  If
you do, you should consider rewriting it.

You must use two blank lines between the last line of a section's body
and the next section heading.  If a subsection heading immediately
follows a section heading, a single blank line in-between is
sufficient.

The body of each section is not normally indented, although some
constructs do use indentation, as described below.  Blank lines are
used to separate constructs.


Paragraphs
----------

Paragraphs are left-aligned text blocks separated by blank lines.
Paragraphs are not indented unless they are part of an indented
construct (such as a block quote or a list item).


Inline Markup
-------------

Portions of text within paragraphs and other text blocks may be
styled.  For example::

    Text may be marked as *emphasized* (single asterisk markup,
    typically shown in italics) or **strongly emphasized** (double
    asterisks, typically boldface).  ``Inline literals`` (using double
    backquotes) are typically rendered in a monospaced typeface.  No
    further markup recognition is done within the double backquotes,
    so they're safe for any kind of code snippets.


Block Quotes
------------

Block quotes consist of indented body elements.  For example::

    This is a paragraph.

        This is a block quote.

        A block quote may contain many paragraphs.

Block quotes are used to quote extended passages from other sources.
Block quotes may be nested inside other body elements.  Use 4 spaces
per indent level.


Literal Blocks
--------------

..  
    In the text below, double backquotes are used to denote inline
    literals.  "``::``" is written so that the colons will appear in a
    monospaced font; the backquotes (``) are markup, not part of the
    text.  See "Inline Markup" above.

    By the way, this is a comment, described in "Comments" below.

Literal blocks are used for code samples or preformatted ASCII art. To
indicate a literal block, preface the indented text block with
"``::``" (two colons).  The literal block continues until the end of
the indentation.  Indent the text block by 4 spaces.  For example::

    This is a typical paragraph.  A literal block follows.

    ::

        for a in [5,4,3,2,1]:   # this is program code, shown as-is
            print a
        print "it's..."
        # a literal block continues until the indentation ends

The paragraph containing only "``::``" will be completely removed from
the output; no empty paragraph will remain.  "``::``" is also
recognized at the end of any paragraph.  If immediately preceded by
whitespace, both colons will be removed from the output.  When text
immediately precedes the "``::``", *one* colon will be removed from
the output, leaving only one colon visible (i.e., "``::``" will be
replaced by "``:``").  For example, one colon will remain visible
here::

    Paragraph::

        Literal block


Lists
-----

Bullet list items begin with one of "-", "*", or "+" (hyphen,
asterisk, or plus sign), followed by whitespace and the list item
body.  List item bodies must be left-aligned and indented relative to
the bullet; the text immediately after the bullet determines the
indentation.  For example::

    This paragraph is followed by a list.

    * This is the first bullet list item.  The blank line above the
      first list item is required; blank lines between list items
      (such as below this paragraph) are optional.

    * This is the first paragraph in the second item in the list.

      This is the second paragraph in the second item in the list.
      The blank line above this paragraph is required.  The left edge
      of this paragraph lines up with the paragraph above, both
      indented relative to the bullet.

      - This is a sublist.  The bullet lines up with the left edge of
        the text blocks above.  A sublist is a new list so requires a
        blank line above and below.

    * This is the third item of the main list.

    This paragraph is not part of the list.

Enumerated (numbered) list items are similar, but use an enumerator
instead of a bullet.  Enumerators are numbers (1, 2, 3, ...), letters
(A, B, C, ...; uppercase or lowercase), or Roman numerals (i, ii, iii,
iv, ...; uppercase or lowercase), formatted with a period suffix
("1.", "2."), parentheses ("(1)", "(2)"), or a right-parenthesis
suffix ("1)", "2)").  For example::

    1. As with bullet list items, the left edge of paragraphs must
       align.

    2. Each list item may contain multiple paragraphs, sublists, etc.

       This is the second paragraph of the second list item.

       a) Enumerated lists may be nested.
       b) Blank lines may be omitted between list items.

Definition lists are written like this::

    what
        Definition lists associate a term with a definition.

    how
        The term is a one-line phrase, and the definition is one
        or more paragraphs or body elements, indented relative to
        the term.


Tables
------

Simple tables are easy and compact::

    =====  =====  =======
      A      B    A and B
    =====  =====  =======
    False  False  False
    True   False  False
    False  True   False
    True   True   True
    =====  =====  =======

There must be at least two columns in a table (to differentiate from
section titles).  Column spans use underlines of hyphens ("Inputs"
spans the first two columns)::

    =====  =====  ======
       Inputs     Output
    ------------  ------
      A      B    A or B
    =====  =====  ======
    False  False  False
    True   False  True
    False  True   True
    True   True   True
    =====  =====  ======

Text in a first-column cell starts a new row.  No text in the first
column indicates a continuation line; the rest of the cells may
consist of multiple lines.  For example::

    =====  =========================
    col 1  col 2
    =====  =========================
    1      Second column of row 1.
    2      Second column of row 2.
           Second line of paragraph.
    3      - Second column of row 3.

           - Second item in bullet
             list (row 3, column 2).
    =====  =========================


Hyperlinks
----------

When referencing an external web page in the body of a PEP, you should
include the title of the page in the text, with either an inline
hyperlink reference to the URL or a footnote reference (see
`Footnotes`_ below).  Do not include the URL in the body text of the
PEP.

Hyperlink references use backquotes and a trailing underscore to mark
up the reference text; backquotes are optional if the reference text
is a single word.  For example::

    In this paragraph, we refer to the `Python web site`_.

An explicit target provides the URL.  Put targets in a References
section at the end of the PEP, or immediately after the reference.
Hyperlink targets begin with two periods and a space (the "explicit
markup start"), followed by a leading underscore, the reference text,
a colon, and the URL (absolute or relative)::

    .. _Python web site: http://www.python.org/

The reference text and the target text must match (although the match
is case-insensitive and ignores differences in whitespace).  Note that
the underscore trails the reference text but precedes the target text.
If you think of the underscore as a right-pointing arrow, it points
*away* from the reference and *toward* the target.

The same mechanism can be used for internal references.  Every unique
section title implicitly defines an internal hyperlink target.  We can
make a link to the Abstract section like this::

    Here is a hyperlink reference to the `Abstract`_ section.  The
    backquotes are optional since the reference text is a single word;
    we can also just write: Abstract_.

Footnotes containing the URLs from external targets will be generated
automatically at the end of the References section of the PEP, along
with footnote references linking the reference text to the footnotes.

Text of the form "PEP x" or "RFC x" (where "x" is a number) will be
linked automatically to the appropriate URLs.


Footnotes
---------

Footnote references consist of a left square bracket, a number, a
right square bracket, and a trailing underscore::

    This sentence ends with a footnote reference [1]_.

Whitespace must precede the footnote reference.  Leave a space between
the footnote reference and the preceding word.

When referring to another PEP, include the PEP number in the body
text, such as "PEP 1".  The title may optionally appear.  Add a
footnote reference following the title.  For example::

    Refer to PEP 1 [2]_ for more information.

Add a footnote that includes the PEP's title and author.  It may
optionally include the explicit URL on a separate line, but only in
the References section.  Footnotes begin with ".. " (the explicit
markup start), followed by the footnote marker (no underscores),
followed by the footnote body.  For example::

    References
    ==========

    .. [2] PEP 1, "PEP Purpose and Guidelines", Warsaw, Hylton
       (http://www.python.org/peps/pep-0001.html)

If you decide to provide an explicit URL for a PEP, please use this as
the URL template::

    http://www.python.org/peps/pep-xxxx.html

PEP numbers in URLs must be padded with zeros from the left, so as to
be exactly 4 characters wide, however PEP numbers in the text are
never padded.

During the course of developing your PEP, you may have to add, remove,
and rearrange footnote references, possibly resulting in mismatched
references, obsolete footnotes, and confusion.  Auto-numbered
footnotes allow more freedom.  Instead of a number, use a label of the
form "#word", where "word" is a mnemonic consisting of alphanumerics
plus internal hyphens, underscores, and periods (no whitespace or
other characters are allowed).  For example::

    Refer to PEP 1 [#PEP-1]_ for more information.

    References
    ==========

    .. [#PEP-1] PEP 1, "PEP Purpose and Guidelines", Warsaw, Hylton

       http://www.python.org/peps/pep-0001.html

Footnotes and footnote references will be numbered automatically, and
the numbers will always match.  Once a PEP is finalized, auto-numbered
labels should be replaced by numbers for simplicity.


Images
------

If your PEP contains a diagram, you may include it in the processed
output using the "image" directive::

    .. image:: diagram.png

Any browser-friendly graphics format is possible: .png, .jpeg, .gif,
.tiff, etc.

Since this image will not be visible to readers of the PEP in source
text form, you should consider including a description or ASCII art
alternative, using a comment (below).


Comments
--------

A comment block is an indented block of arbitrary text immediately
following an explicit markup start: two periods and whitespace.  Leave
the ".." on a line by itself to ensure that the comment is not
misinterpreted as another explicit markup construct.  Comments are not
visible in the processed document.  For the benefit of those reading
your PEP in source form, please consider including a descriptions of
or ASCII art alternatives to any images you include.  For example::

     .. image:: dataflow.png

     ..
        Data flows from the input module, through the "black box"
        module, and finally into (and through) the output module.

The Emacs stanza at the bottom of this document is inside a comment.


Escaping Mechanism
------------------

reStructuredText uses backslashes ("``\``") to override the special
meaning given to markup characters and get the literal characters
themselves.  To get a literal backslash, use an escaped backslash
("``\\``").  There are two contexts in which backslashes have no
special meaning: `literal blocks`_ and inline literals (see `Inline
Markup`_ above).  In these contexts, no markup recognition is done,
and a single backslash represents a literal backslash, without having
to double up.

If you find that you need to use a backslash in your text, consider
using inline literals or a literal block instead.


Habits to Avoid
===============

Many programmers who are familiar with TeX often write quotation marks
like this::

    `single-quoted' or ``double-quoted''

Backquotes are significant in reStructuredText, so this practice
should be avoided.  For ordinary text, use ordinary 'single-quotes' or
"double-quotes".  For inline literal text (see `Inline Markup`_
above), use double-backquotes::

    ``literal text: in here, anything goes!``


Resources
=========

Many other constructs and variations are possible.  For more details
about the reStructuredText markup, in increasing order of
thoroughness, please see:

* `A ReStructuredText Primer`__, a gentle introduction.

  __ http://docutils.sourceforge.net/docs/rst/quickstart.html

* `Quick reStructuredText`__, a users' quick reference.

  __ http://docutils.sourceforge.net/docs/rst/quickref.html

* `reStructuredText Markup Specification`__, the final authority.

  __ http://docutils.sourceforge.net/spec/rst/reStructuredText.html

The processing of reStructuredText PEPs is done using Docutils_.  If
you have a question or require assistance with reStructuredText or
Docutils, please `post a message`_ to the `Docutils-Users mailing
list`_.  The `Docutils project web site`_ has more information.

.. _Docutils: http://docutils.sourceforge.net/
.. _post a message:
   mailto:docutils-users@lists.sourceforge.net?subject=PEPs
.. _Docutils-Users mailing list:
   http://lists.sourceforge.net/lists/listinfo/docutils-users
.. _Docutils project web site: http://docutils.sourceforge.net/


References
==========

.. [1] PEP 1, PEP Purpose and Guidelines, Warsaw, Hylton
   (http://www.python.org/peps/pep-0001.html)

.. [2] PEP 9, Sample Plaintext PEP Template, Warsaw
   (http://www.python.org/peps/pep-0009.html)


Copyright
=========

This document has been placed in the public domain.



..
   Local Variables:
   mode: indented-text
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   End:
````

</details>

<details><summary><b>Step 2 — revision_2</b> (3418 words)</summary>

````text
.. note::
    For those who have written a PEP before, there is a template_
    (which is included as a file in the PEPs repository).

Abstract
========

This PEP provides a boilerplate or sample template for creating your
own reStructuredText PEPs.  In conjunction with the content guidelines
in PEP 1 [1]_, this should make it easy for you to conform your own
PEPs to the format outlined below.

Note: if you are reading this PEP via the web, you should first grab
the text (reStructuredText) source of this PEP in order to complete
the steps below.  **DO NOT USE THE HTML FILE AS YOUR TEMPLATE!**

The source for this (or any) PEP can be found in the PEPs repository,
viewable on the web at https://github.com/python/peps/ .


Rationale
=========

If you intend to submit a PEP, you MUST use this template, in
conjunction with the format guidelines below, to ensure that your PEP
submission won't get automatically rejected because of form.

ReStructuredText provides PEP authors with useful functionality and
expressivity, while maintaining easy readability in the source text.
The processed HTML form makes the functionality accessible to readers:
live hyperlinks, styled text, tables, images, and automatic tables of
contents, among other advantages.


How to Use This Template
========================

To use this template you must first decide whether your PEP is going
to be an Informational or Standards Track PEP.  Most PEPs are
Standards Track because they propose a new feature for the Python
language or standard library.  When in doubt, read PEP 1 for details,
or open a tracker issue on the PEPs repo to ask for assistance.

Once you've decided which type of PEP yours is going to be, follow the
directions below.

- Make a copy of this file (the ``.rst`` file, **not** the HTML!) and
  perform the following edits. Name the new file ``pep-9999.rst`` if
  you don't yet have a PEP number assignment, or ``pep-NNNN.rst`` if
  you do. Those with push permissions are welcome to claim the next
  available number (ignoring the special blocks 3000 and 8000, and a
  handful of special allocations - currently 666, 754, and 801) and
  push it directly.

- Replace the "PEP: 12" header with "PEP: 9999" or "PEP: NNNN",
  matching the file name. Note that the file name should be padded with
  zeros (eg ``pep-0012.rst``), but the header should not (``PEP: 12``).

- Change the Title header to the title of your PEP.

- Change the Author header to include your name, and optionally your
  email address.  Be sure to follow the format carefully: your name
  must appear first, and it must not be contained in parentheses.
  Your email address may appear second (or it can be omitted) and if
  it appears, it must appear in angle brackets.  It is okay to
  obfuscate your email address.

- If none of the authors are Python core developers, include a Sponsor
  header with the name of the core developer sponsoring your PEP.

- For many PEPs, discussions will take place on python-ideas@python.org
  and/or python-dev@python.org. If there is another mailing list or
  public forum more appropriate for discussion of your new feature,
  add a Discussions-To header right after the Author header. Most
  Informational PEPs don't need a Discussions-To header.

- Change the Status header to "Draft".

- For Standards Track PEPs, change the Type header to "Standards
  Track".

- For Informational PEPs, change the Type header to "Informational".

- For Standards Track PEPs, if your feature depends on the acceptance
  of some other currently in-development PEP, add a Requires header
  right after the Type header.  The value should be the PEP number of
  the PEP yours depends on.  Don't add this header if your dependent
  feature is described in a Final PEP.

- Change the Created header to today's date.  Be sure to follow the
  format carefully: it must be in ``dd-mmm-yyyy`` format, where the
  ``mmm`` is the 3 English letter month abbreviation, i.e. one of Jan,
  Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec.

- For Standards Track PEPs, after the Created header, add a
  Python-Version header and set the value to the next planned version
  of Python, i.e. the one your new feature will hopefully make its
  first appearance in.  Do not use an alpha or beta release
  designation here.  Thus, if the last version of Python was 2.2 alpha
  1 and you're hoping to get your new feature into Python 2.2, set the
  header to::

      Python-Version: 2.2

- Leave Post-History alone for now; you'll add dates to this header
  each time you post your PEP to the designated discussion forum (see
  the Discussions-To header above). If you posted your PEP to the lists
  on August 14, 2001 and September 3, 2001, the Post-History header
  would look like::

      Post-History: 14-Aug-2001, 03-Sept-2001

  You must manually add new dates and commit them (with a pull request
  if you don't have push privileges).

- Add a Replaces header if your PEP obsoletes an earlier PEP.  The
  value of this header is the number of the PEP that your new PEP is
  replacing.  Only add this header if the older PEP is in "final"
  form, i.e. is either Accepted, Final, or Rejected.  You aren't
  replacing an older open PEP if you're submitting a competing idea.

- Now write your Abstract, Rationale, and other content for your PEP,
  replacing all this gobbledygook with your own text. Be sure to
  adhere to the format guidelines below, specifically on the
  prohibition of tab characters and the indentation requirements.
  See "Suggested Sections" below for a template of sections to include.

- Update your References and Copyright section.  Usually you'll place
  your PEP into the public domain, in which case just leave the
  Copyright section alone.  Alternatively, you can use the `Open
  Publication License`__, but public domain is still strongly
  preferred.

  __ http://www.opencontent.org/openpub/

- Leave the Emacs stanza at the end of this file alone, including the
  formfeed character ("^L", or ``\f``).

- Create a pull request against the https://github.com/python/peps
  repository.

For reference, here are all of the possible header fields (everything
in brackets should either be replaced or have the field removed if
it has a leading ``*`` marking it as optional and it does not apply to
your PEP)::

  PEP: [NNN]
  Title: [...]
  Author: [Full Name <email at example.com>]
  Sponsor: *[Full Name <email at example.com>]
  PEP-Delegate:
  Discussions-To: *[...]
  Status: Draft
  Type: [Standards Track | Informational | Process]
  Content-Type: text/x-rst
  Requires: *[NNN]
  Created: [DD-MMM-YYYY]
  Python-Version: *[M.N]
  Post-History: [DD-MMM-YYYY]
  Replaces: *[NNN]
  Superseded-By: *[NNN]
  Resolution:


ReStructuredText PEP Formatting Requirements
============================================

The following is a PEP-specific summary of reStructuredText syntax.
For the sake of simplicity and brevity, much detail is omitted.  For
more detail, see `Resources`_ below.  `Literal blocks`_ (in which no
markup processing is done) are used for examples throughout, to
illustrate the plaintext markup.


General
-------

You must adhere to the Emacs convention of adding two spaces at the
end of every sentence.  You should fill your paragraphs to column 70,
but under no circumstances should your lines extend past column 79.
If your code samples spill over column 79, you should rewrite them.

Tab characters must never appear in the document at all.  A PEP should
include the standard Emacs stanza included by example at the bottom of
this PEP.


Section Headings
----------------

PEP headings must begin in column zero and the initial letter of each
word must be capitalized as in book titles.  Acronyms should be in all
capitals.  Section titles must be adorned with an underline, a single
repeated punctuation character, which begins in column zero and must
extend at least as far as the right edge of the title text (4
characters minimum).  First-level section titles are underlined with
"=" (equals signs), second-level section titles with "-" (hyphens),
and third-level section titles with "'" (single quotes or
apostrophes).  For example::

    First-Level Title
    =================

    Second-Level Title
    ------------------

    Third-Level Title
    '''''''''''''''''

If there are more than three levels of sections in your PEP, you may
insert overline/underline-adorned titles for the first and second
levels as follows::

    ============================
    First-Level Title (optional)
    ============================

    -----------------------------
    Second-Level Title (optional)
    -----------------------------

    Third-Level Title
    =================

    Fourth-Level Title
    ------------------

    Fifth-Level Title
    '''''''''''''''''

You shouldn't have more than five levels of sections in your PEP.  If
you do, you should consider rewriting it.

You must use two blank lines between the last line of a section's body
and the next section heading.  If a subsection heading immediately
follows a section heading, a single blank line in-between is
sufficient.

The body of each section is not normally indented, although some
constructs do use indentation, as described below.  Blank lines are
used to separate constructs.


Paragraphs
----------

Paragraphs are left-aligned text blocks separated by blank lines.
Paragraphs are not indented unless they are part of an indented
construct (such as a block quote or a list item).


Inline Markup
-------------

Portions of text within paragraphs and other text blocks may be
styled.  For example::

    Text may be marked as *emphasized* (single asterisk markup,
    typically shown in italics) or **strongly emphasized** (double
    asterisks, typically boldface).  ``Inline literals`` (using double
    backquotes) are typically rendered in a monospaced typeface.  No
    further markup recognition is done within the double backquotes,
    so they're safe for any kind of code snippets.


Block Quotes
------------

Block quotes consist of indented body elements.  For example::

    This is a paragraph.

        This is a block quote.

        A block quote may contain many paragraphs.

Block quotes are used to quote extended passages from other sources.
Block quotes may be nested inside other body elements.  Use 4 spaces
per indent level.


Literal Blocks
--------------

..
    In the text below, double backquotes are used to denote inline
    literals.  "``::``" is written so that the colons will appear in a
    monospaced font; the backquotes (``) are markup, not part of the
    text.  See "Inline Markup" above.

    By the way, this is a comment, described in "Comments" below.

Literal blocks are used for code samples or preformatted ASCII art. To
indicate a literal block, preface the indented text block with
"``::``" (two colons).  The literal block continues until the end of
the indentation.  Indent the text block by 4 spaces.  For example::

    This is a typical paragraph.  A literal block follows.

    ::

        for a in [5,4,3,2,1]:   # this is program code, shown as-is
            print a
        print "it's..."
        # a literal block continues until the indentation ends

The paragraph containing only "``::``" will be completely removed from
the output; no empty paragraph will remain.  "``::``" is also
recognized at the end of any paragraph.  If immediately preceded by
whitespace, both colons will be removed from the output.  When text
immediately precedes the "``::``", *one* colon will be removed from
the output, leaving only one colon visible (i.e., "``::``" will be
replaced by "``:``").  For example, one colon will remain visible
here::

    Paragraph::

        Literal block


Lists
-----

Bullet list items begin with one of "-", "*", or "+" (hyphen,
asterisk, or plus sign), followed by whitespace and the list item
body.  List item bodies must be left-aligned and indented relative to
the bullet; the text immediately after the bullet determines the
indentation.  For example::

    This paragraph is followed by a list.

    * This is the first bullet list item.  The blank line above the
      first list item is required; blank lines between list items
      (such as below this paragraph) are optional.

    * This is the first paragraph in the second item in the list.

      This is the second paragraph in the second item in the list.
      The blank line above this paragraph is required.  The left edge
      of this paragraph lines up with the paragraph above, both
      indented relative to the bullet.

      - This is a sublist.  The bullet lines up with the left edge of
        the text blocks above.  A sublist is a new list so requires a
        blank line above and below.

    * This is the third item of the main list.

    This paragraph is not part of the list.

Enumerated (numbered) list items are similar, but use an enumerator
instead of a bullet.  Enumerators are numbers (1, 2, 3, ...), letters
(A, B, C, ...; uppercase or lowercase), or Roman numerals (i, ii, iii,
iv, ...; uppercase or lowercase), formatted with a period suffix
("1.", "2."), parentheses ("(1)", "(2)"), or a right-parenthesis
suffix ("1)", "2)").  For example::

    1. As with bullet list items, the left edge of paragraphs must
       align.

    2. Each list item may contain multiple paragraphs, sublists, etc.

       This is the second paragraph of the second list item.

       a) Enumerated lists may be nested.
       b) Blank lines may be omitted between list items.

Definition lists are written like this::

    what
        Definition lists associate a term with a definition.

    how
        The term is a one-line phrase, and the definition is one
        or more paragraphs or body elements, indented relative to
        the term.


Tables
------

Simple tables are easy and compact::

    =====  =====  =======
      A      B    A and B
    =====  =====  =======
    False  False  False
    True   False  False
    False  True   False
    True   True   True
    =====  =====  =======

There must be at least two columns in a table (to differentiate from
section titles).  Column spans use underlines of hyphens ("Inputs"
spans the first two columns)::

    =====  =====  ======
       Inputs     Output
    ------------  ------
      A      B    A or B
    =====  =====  ======
    False  False  False
    True   False  True
    False  True   True
    True   True   True
    =====  =====  ======

Text in a first-column cell starts a new row.  No text in the first
column indicates a continuation line; the rest of the cells may
consist of multiple lines.  For example::

    =====  =========================
    col 1  col 2
    =====  =========================
    1      Second column of row 1.
    2      Second column of row 2.
           Second line of paragraph.
    3      - Second column of row 3.

           - Second item in bullet
             list (row 3, column 2).
    =====  =========================


Hyperlinks
----------

When referencing an external web page in the body of a PEP, you should
include the title of the page in the text, with either an inline
hyperlink reference to the URL or a footnote reference (see
`Footnotes`_ below).  Do not include the URL in the body text of the
PEP.

Hyperlink references use backquotes and a trailing underscore to mark
up the reference text; backquotes are optional if the reference text
is a single word.  For example::

    In this paragraph, we refer to the `Python web site`_.

An explicit target provides the URL.  Put targets in a References
section at the end of the PEP, or immediately after the reference.
Hyperlink targets begin with two periods and a space (the "explicit
markup start"), followed by a leading underscore, the reference text,
a colon, and the URL (absolute or relative)::

    .. _Python web site: http://www.python.org/

The reference text and the target text must match (although the match
is case-insensitive and ignores differences in whitespace).  Note that
the underscore trails the reference text but precedes the target text.
If you think of the underscore as a right-pointing arrow, it points
*away* from the reference and *toward* the target.

The same mechanism can be used for internal references.  Every unique
section title implicitly defines an internal hyperlink target.  We can
make a link to the Abstract section like this::

    Here is a hyperlink reference to the `Abstract`_ section.  The
    backquotes are optional since the reference text is a single word;
    we can also just write: Abstract_.

Footnotes containing the URLs from external targets will be generated
automatically at the end of the References section of the PEP, along
with footnote references linking the reference text to the footnotes.

Text of the form "PEP x" or "RFC x" (where "x" is a number) will be
linked automatically to the appropriate URLs.


Footnotes
---------

Footnote references consist of a left square bracket, a number, a
right square bracket, and a trailing underscore::

    This sentence ends with a footnote reference [1]_.

Whitespace must precede the footnote reference.  Leave a space between
the footnote reference and the preceding word.

When referring to another PEP, include the PEP number in the body
text, such as "PEP 1".  The title may optionally appear.  Add a
footnote reference following the title.  For example::

    Refer to PEP 1 [2]_ for more information.

Add a footnote that includes the PEP's title and author.  It may
optionally include the explicit URL on a separate line, but only in
the References section.  Footnotes begin with ".. " (the explicit
markup start), followed by the footnote marker (no underscores),
followed by the footnote body.  For example::

    References
    ==========

    .. [2] PEP 1, "PEP Purpose and Guidelines", Warsaw, Hylton
       (http://www.python.org/dev/peps/pep-0001)

If you decide to provide an explicit URL for a PEP, please use this as
the URL template::

    http://www.python.org/dev/peps/pep-xxxx

PEP numbers in URLs must be padded with zeros from the left, so as to
be exactly 4 characters wide; however, PEP numbers in the text are
never padded.

During the course of developing your PEP, you may have to add, remove,
and rearrange footnote references, possibly resulting in mismatched
references, obsolete footnotes, and confusion.  Auto-numbered
footnotes allow more freedom.  Instead of a number, use a label of the
form "#word", where "word" is a mnemonic consisting of alphanumerics
plus internal hyphens, underscores, and periods (no whitespace or
other characters are allowed).  For example::

    Refer to PEP 1 [#PEP-1]_ for more information.

    References
    ==========

    .. [#PEP-1] PEP 1, "PEP Purpose and Guidelines", Warsaw, Hylton

       http://www.python.org/dev/peps/pep-0001

Footnotes and footnote references will be numbered automatically, and
the numbers will always match.  Once a PEP is finalized, auto-numbered
labels should be replaced by numbers for simplicity.


Images
------

If your PEP contains a diagram, you may include it in the processed
output using the "image" directive::

    .. image:: diagram.png

Any browser-friendly graphics format is possible: .png, .jpeg, .gif,
.tiff, etc.

Since this image will not be visible to readers of the PEP in source
text form, you should consider including a description or ASCII art
alternative, using a comment (below).


Comments
--------

A comment block is an indented block of arbitrary text immediately
following an explicit markup start: two periods and whitespace.  Leave
the ".." on a line by itself to ensure that the comment is not
misinterpreted as another explicit markup construct.  Comments are not
visible in the processed document.  For the benefit of those reading
your PEP in source form, please consider including a descriptions of
or ASCII art alternatives to any images you include.  For example::

     .. image:: dataflow.png

     ..
        Data flows from the input module, through the "black box"
        module, and finally into (and through) the output module.

The Emacs stanza at the bottom of this document is inside a comment.


Escaping Mechanism
------------------

reStructuredText uses backslashes ("``\``") to override the special
meaning given to markup characters and get the literal characters
themselves.  To get a literal backslash, use an escaped backslash
("``\\``").  There are two contexts in which backslashes have no
special meaning: `literal blocks`_ and inline literals (see `Inline
Markup`_ above).  In these contexts, no markup recognition is done,
and a single backslash represents a literal backslash, without having
to double up.

If you find that you need to use a backslash in your text, consider
using inline literals or a literal block instead.


Habits to Avoid
===============

Many programmers who are familiar with TeX often write quotation marks
like this::

    `single-quoted' or ``double-quoted''

Backquotes are significant in reStructuredText, so this practice
should be avoided.  For ordinary text, use ordinary 'single-quotes' or
"double-quotes".  For inline literal text (see `Inline Markup`_
above), use double-backquotes::

    ``literal text: in here, anything goes!``


Suggested Sections
==================

Various sections are found to be common across PEPs and are outlined in
PEP 1 [1]_. Those sections are provided here for convenience.

.. _template:

.. _include:: pep-0012/pep-NNNN.rst
   :literal:


Resources
=========

Many other constructs and variations are possible.  For more details
about the reStructuredText markup, in increasing order of
thoroughness, please see:

* `A ReStructuredText Primer`__, a gentle introduction.

  __ http://docutils.sourceforge.net/docs/rst/quickstart.html

* `Quick reStructuredText`__, a users' quick reference.

  __ http://docutils.sourceforge.net/docs/rst/quickref.html

* `reStructuredText Markup Specification`__, the final authority.

  __ http://docutils.sourceforge.net/spec/rst/reStructuredText.html

The processing of reStructuredText PEPs is done using Docutils_.  If
you have a question or require assistance with reStructuredText or
Docutils, please `post a message`_ to the `Docutils-users mailing
list`_.  The `Docutils project web site`_ has more information.

.. _Docutils:
.. _Docutils project web site: http://docutils.sourceforge.net/
.. _post a message:
   mailto:docutils-users@lists.sourceforge.net?subject=PEPs
.. _Docutils-users mailing list:
   http://docutils.sf.net/docs/user/mailing-lists.html#docutils-users


References
==========

.. [1] PEP 1, PEP Purpose and Guidelines, Warsaw, Hylton
   (http://www.python.org/dev/peps/pep-0001)


Copyright
=========

This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.



..
   Local Variables:
   mode: indented-text
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   coding: utf-8
   End:
````

</details>

<details><summary><b>Step 3 — revision_3</b> (3371 words)</summary>

````text
.. note::
    For those who have written a PEP before, there is a template_
    (which is included as a file in the PEPs repository).

Abstract
========

This PEP provides a boilerplate or sample template for creating your
own reStructuredText PEPs.  In conjunction with the content guidelines
in :pep:`1`, this should make it easy for you to conform your own
PEPs to the format outlined below.

Note: if you are reading this PEP via the web, you should first grab
the text (reStructuredText) source of this PEP in order to complete
the steps below.  **DO NOT USE THE HTML FILE AS YOUR TEMPLATE!**

The source for this (or any) PEP can be found in the PEPs repository,
viewable on the web at https://github.com/python/peps/ .


Rationale
=========

If you intend to submit a PEP, you MUST use this template, in
conjunction with the format guidelines below, to ensure that your PEP
submission won't get automatically rejected because of form.

ReStructuredText provides PEP authors with useful functionality and
expressivity, while maintaining easy readability in the source text.
The processed HTML form makes the functionality accessible to readers:
live hyperlinks, styled text, tables, images, and automatic tables of
contents, among other advantages.


How to Use This Template
========================

To use this template you must first decide whether your PEP is going
to be an Informational or Standards Track PEP.  Most PEPs are
Standards Track because they propose a new feature for the Python
language or standard library.  When in doubt, read :pep:`1` for details,
or open a tracker issue on the PEPs repo to ask for assistance.

Once you've decided which type of PEP yours is going to be, follow the
directions below.

- Make a copy of this file (the ``.rst`` file, **not** the HTML!) and
  perform the following edits. Name the new file ``pep-9999.rst`` if
  you don't yet have a PEP number assignment, or ``pep-NNNN.rst`` if
  you do. Those with push permissions are welcome to claim the next
  available number (ignoring the special blocks 3000 and 8000, and a
  handful of special allocations - currently 666, 754, and 801) and
  push it directly.

- Replace the "PEP: 12" header with "PEP: 9999" or "PEP: NNNN",
  matching the file name. Note that the file name should be padded with
  zeros (eg ``pep-0012.rst``), but the header should not (``PEP: 12``).

- Change the Title header to the title of your PEP.

- Change the Author header to include your name, and optionally your
  email address.  Be sure to follow the format carefully: your name
  must appear first, and it must not be contained in parentheses.
  Your email address may appear second (or it can be omitted) and if
  it appears, it must appear in angle brackets.  It is okay to
  obfuscate your email address.

- If none of the authors are Python core developers, include a Sponsor
  header with the name of the core developer sponsoring your PEP.

- For many PEPs, discussions will take place on python-ideas@python.org
  and/or python-dev@python.org. If there is another mailing list or
  public forum more appropriate for discussion of your new feature,
  add a Discussions-To header right after the Author header. Most
  Informational PEPs don't need a Discussions-To header.

- Change the Status header to "Draft".

- For Standards Track PEPs, change the Type header to "Standards
  Track".

- For Informational PEPs, change the Type header to "Informational".

- For Standards Track PEPs, if your feature depends on the acceptance
  of some other currently in-development PEP, add a Requires header
  right after the Type header.  The value should be the PEP number of
  the PEP yours depends on.  Don't add this header if your dependent
  feature is described in a Final PEP.

- Change the Created header to today's date.  Be sure to follow the
  format carefully: it must be in ``dd-mmm-yyyy`` format, where the
  ``mmm`` is the 3 English letter month abbreviation, i.e. one of Jan,
  Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec.

- For Standards Track PEPs, after the Created header, add a
  Python-Version header and set the value to the next planned version
  of Python, i.e. the one your new feature will hopefully make its
  first appearance in.  Do not use an alpha or beta release
  designation here.  Thus, if the last version of Python was 2.2 alpha
  1 and you're hoping to get your new feature into Python 2.2, set the
  header to::

      Python-Version: 2.2

- Leave Post-History alone for now; you'll add dates to this header
  each time you post your PEP to the designated discussion forum (see
  the Discussions-To header above). If you posted your PEP to the lists
  on August 14, 2001 and September 3, 2001, the Post-History header
  would look like::

      Post-History: 14-Aug-2001, 03-Sept-2001

  You must manually add new dates and commit them (with a pull request
  if you don't have push privileges).

- Add a Replaces header if your PEP obsoletes an earlier PEP.  The
  value of this header is the number of the PEP that your new PEP is
  replacing.  Only add this header if the older PEP is in "final"
  form, i.e. is either Accepted, Final, or Rejected.  You aren't
  replacing an older open PEP if you're submitting a competing idea.

- Now write your Abstract, Rationale, and other content for your PEP,
  replacing all this gobbledygook with your own text. Be sure to
  adhere to the format guidelines below, specifically on the
  prohibition of tab characters and the indentation requirements.
  See "Suggested Sections" below for a template of sections to include.

- Update your References and Copyright section.  Usually you'll place
  your PEP into the public domain, in which case just leave the
  Copyright section alone.  Alternatively, you can use the `Open
  Publication License`__, but public domain is still strongly
  preferred.

  __ http://www.opencontent.org/openpub/

- Leave the Emacs stanza at the end of this file alone, including the
  formfeed character ("^L", or ``\f``).

- Create a pull request against the https://github.com/python/peps
  repository.

For reference, here are all of the possible header fields (everything
in brackets should either be replaced or have the field removed if
it has a leading ``*`` marking it as optional and it does not apply to
your PEP)::

  PEP: [NNN]
  Title: [...]
  Author: [Full Name <email at example.com>]
  Sponsor: *[Full Name <email at example.com>]
  PEP-Delegate:
  Discussions-To: *[...]
  Status: Draft
  Type: [Standards Track | Informational | Process]
  Content-Type: text/x-rst
  Requires: *[NNN]
  Created: [DD-MMM-YYYY]
  Python-Version: *[M.N]
  Post-History: [DD-MMM-YYYY]
  Replaces: *[NNN]
  Superseded-By: *[NNN]
  Resolution:


ReStructuredText PEP Formatting Requirements
============================================

The following is a PEP-specific summary of reStructuredText syntax.
For the sake of simplicity and brevity, much detail is omitted.  For
more detail, see `Resources`_ below.  `Literal blocks`_ (in which no
markup processing is done) are used for examples throughout, to
illustrate the plaintext markup.


General
-------

You must adhere to the Emacs convention of adding two spaces at the
end of every sentence.  You should fill your paragraphs to column 70,
but under no circumstances should your lines extend past column 79.
If your code samples spill over column 79, you should rewrite them.

Tab characters must never appear in the document at all.  A PEP should
include the standard Emacs stanza included by example at the bottom of
this PEP.


Section Headings
----------------

PEP headings must begin in column zero and the initial letter of each
word must be capitalized as in book titles.  Acronyms should be in all
capitals.  Section titles must be adorned with an underline, a single
repeated punctuation character, which begins in column zero and must
extend at least as far as the right edge of the title text (4
characters minimum).  First-level section titles are underlined with
"=" (equals signs), second-level section titles with "-" (hyphens),
and third-level section titles with "'" (single quotes or
apostrophes).  For example::

    First-Level Title
    =================

    Second-Level Title
    ------------------

    Third-Level Title
    '''''''''''''''''

If there are more than three levels of sections in your PEP, you may
insert overline/underline-adorned titles for the first and second
levels as follows::

    ============================
    First-Level Title (optional)
    ============================

    -----------------------------
    Second-Level Title (optional)
    -----------------------------

    Third-Level Title
    =================

    Fourth-Level Title
    ------------------

    Fifth-Level Title
    '''''''''''''''''

You shouldn't have more than five levels of sections in your PEP.  If
you do, you should consider rewriting it.

You must use two blank lines between the last line of a section's body
and the next section heading.  If a subsection heading immediately
follows a section heading, a single blank line in-between is
sufficient.

The body of each section is not normally indented, although some
constructs do use indentation, as described below.  Blank lines are
used to separate constructs.


Paragraphs
----------

Paragraphs are left-aligned text blocks separated by blank lines.
Paragraphs are not indented unless they are part of an indented
construct (such as a block quote or a list item).


Inline Markup
-------------

Portions of text within paragraphs and other text blocks may be
styled.  For example::

    Text may be marked as *emphasized* (single asterisk markup,
    typically shown in italics) or **strongly emphasized** (double
    asterisks, typically boldface).  ``Inline literals`` (using double
    backquotes) are typically rendered in a monospaced typeface.  No
    further markup recognition is done within the double backquotes,
    so they're safe for any kind of code snippets.


Block Quotes
------------

Block quotes consist of indented body elements.  For example::

    This is a paragraph.

        This is a block quote.

        A block quote may contain many paragraphs.

Block quotes are used to quote extended passages from other sources.
Block quotes may be nested inside other body elements.  Use 4 spaces
per indent level.


Literal Blocks
--------------

..
    In the text below, double backquotes are used to denote inline
    literals.  "``::``" is written so that the colons will appear in a
    monospaced font; the backquotes (``) are markup, not part of the
    text.  See "Inline Markup" above.

    By the way, this is a comment, described in "Comments" below.

Literal blocks are used for code samples or preformatted ASCII art. To
indicate a literal block, preface the indented text block with
"``::``" (two colons).  The literal block continues until the end of
the indentation.  Indent the text block by 4 spaces.  For example::

    This is a typical paragraph.  A literal block follows.

    ::

        for a in [5,4,3,2,1]:   # this is program code, shown as-is
            print a
        print "it's..."
        # a literal block continues until the indentation ends

The paragraph containing only "``::``" will be completely removed from
the output; no empty paragraph will remain.  "``::``" is also
recognized at the end of any paragraph.  If immediately preceded by
whitespace, both colons will be removed from the output.  When text
immediately precedes the "``::``", *one* colon will be removed from
the output, leaving only one colon visible (i.e., "``::``" will be
replaced by "``:``").  For example, one colon will remain visible
here::

    Paragraph::

        Literal block


Lists
-----

Bullet list items begin with one of "-", "*", or "+" (hyphen,
asterisk, or plus sign), followed by whitespace and the list item
body.  List item bodies must be left-aligned and indented relative to
the bullet; the text immediately after the bullet determines the
indentation.  For example::

    This paragraph is followed by a list.

    * This is the first bullet list item.  The blank line above the
      first list item is required; blank lines between list items
      (such as below this paragraph) are optional.

    * This is the first paragraph in the second item in the list.

      This is the second paragraph in the second item in the list.
      The blank line above this paragraph is required.  The left edge
      of this paragraph lines up with the paragraph above, both
      indented relative to the bullet.

      - This is a sublist.  The bullet lines up with the left edge of
        the text blocks above.  A sublist is a new list so requires a
        blank line above and below.

    * This is the third item of the main list.

    This paragraph is not part of the list.

Enumerated (numbered) list items are similar, but use an enumerator
instead of a bullet.  Enumerators are numbers (1, 2, 3, ...), letters
(A, B, C, ...; uppercase or lowercase), or Roman numerals (i, ii, iii,
iv, ...; uppercase or lowercase), formatted with a period suffix
("1.", "2."), parentheses ("(1)", "(2)"), or a right-parenthesis
suffix ("1)", "2)").  For example::

    1. As with bullet list items, the left edge of paragraphs must
       align.

    2. Each list item may contain multiple paragraphs, sublists, etc.

       This is the second paragraph of the second list item.

       a) Enumerated lists may be nested.
       b) Blank lines may be omitted between list items.

Definition lists are written like this::

    what
        Definition lists associate a term with a definition.

    how
        The term is a one-line phrase, and the definition is one
        or more paragraphs or body elements, indented relative to
        the term.


Tables
------

Simple tables are easy and compact::

    =====  =====  =======
      A      B    A and B
    =====  =====  =======
    False  False  False
    True   False  False
    False  True   False
    True   True   True
    =====  =====  =======

There must be at least two columns in a table (to differentiate from
section titles).  Column spans use underlines of hyphens ("Inputs"
spans the first two columns)::

    =====  =====  ======
       Inputs     Output
    ------------  ------
      A      B    A or B
    =====  =====  ======
    False  False  False
    True   False  True
    False  True   True
    True   True   True
    =====  =====  ======

Text in a first-column cell starts a new row.  No text in the first
column indicates a continuation line; the rest of the cells may
consist of multiple lines.  For example::

    =====  =========================
    col 1  col 2
    =====  =========================
    1      Second column of row 1.
    2      Second column of row 2.
           Second line of paragraph.
    3      - Second column of row 3.

           - Second item in bullet
             list (row 3, column 2).
    =====  =========================


Hyperlinks
----------

When referencing an external web page in the body of a PEP, you should
include the title of the page in the text, with either an inline
hyperlink reference to the URL or a footnote reference (see
`Footnotes`_ below).  Do not include the URL in the body text of the
PEP.

Hyperlink references use backquotes and a trailing underscore to mark
up the reference text; backquotes are optional if the reference text
is a single word.  For example::

    In this paragraph, we refer to the `Python web site`_.

An explicit target provides the URL.  Put targets in a References
section at the end of the PEP, or immediately after the reference.
Hyperlink targets begin with two periods and a space (the "explicit
markup start"), followed by a leading underscore, the reference text,
a colon, and the URL (absolute or relative)::

    .. _Python web site: http://www.python.org/

The reference text and the target text must match (although the match
is case-insensitive and ignores differences in whitespace).  Note that
the underscore trails the reference text but precedes the target text.
If you think of the underscore as a right-pointing arrow, it points
*away* from the reference and *toward* the target.

The same mechanism can be used for internal references.  Every unique
section title implicitly defines an internal hyperlink target.  We can
make a link to the Abstract section like this::

    Here is a hyperlink reference to the `Abstract`_ section.  The
    backquotes are optional since the reference text is a single word;
    we can also just write: Abstract_.

Footnotes containing the URLs from external targets will be generated
automatically at the end of the References section of the PEP, along
with footnote references linking the reference text to the footnotes.

To refer to PEPs or RFCs, always use the ``:pep:`` and ``:rfc:`` roles,
never hardcoded URLs.
For example:

.. code-block:: rst

    See :pep:`1` for more information on how to write a PEP,
    and :pep:`the Hyperlink section of PEP 12 <12#hyperlinks>` for how to link.

This renders as:

    See :pep:`1` for more information on how to write a PEP,
    and :pep:`the Hyperlink section of PEP 12 <12#hyperlinks>` for how to link.

PEP numbers in the text are never padded, and there is a space (not a dash)
between "PEP" or "RFC" and the number; the above roles will take care of
that for you.


Footnotes
---------

Footnote references consist of a left square bracket, a number, a
right square bracket, and a trailing underscore:

.. code-block:: rst

    This sentence ends with a footnote reference [1]_.

Whitespace must precede the footnote reference.  Leave a space between
the footnote reference and the preceding word.

Footnotes begin with ".. " (the explicit
markup start), followed by the footnote marker (no underscores),
followed by the footnote body.  For example:

.. code-block:: rst

    References
    ==========

    .. [1] Note that the footnote reference is a numbered one.

    .. [2] Donald Knuth's *The TeXbook*, pages 195 and 196.

During the course of developing your PEP, you may have to add, remove,
and rearrange footnote references, possibly resulting in mismatched
references, obsolete footnotes, and confusion.  Auto-numbered
footnotes allow more freedom.  Instead of a number, use a label of the
form "#word", where "word" is a mnemonic consisting of alphanumerics
plus internal hyphens, underscores, and periods (no whitespace or
other characters are allowed).  For example:

.. code-block:: rst

    Refer to The TeXbook [#TeXbook]_ for more information.

    References
    ==========

    .. [#TeXbook] Donald Knuth's *The TeXbook*, pages 195 and 196.


Footnotes and footnote references will be numbered automatically, and
the numbers will always match.


Images
------

If your PEP contains a diagram, you may include it in the processed
output using the "image" directive::

    .. image:: diagram.png

Any browser-friendly graphics format is possible: .png, .jpeg, .gif,
.tiff, etc.

Since this image will not be visible to readers of the PEP in source
text form, you should consider including a description or ASCII art
alternative, using a comment (below).


Comments
--------

A comment block is an indented block of arbitrary text immediately
following an explicit markup start: two periods and whitespace.  Leave
the ".." on a line by itself to ensure that the comment is not
misinterpreted as another explicit markup construct.  Comments are not
visible in the processed document.  For the benefit of those reading
your PEP in source form, please consider including a descriptions of
or ASCII art alternatives to any images you include.  For example::

     .. image:: dataflow.png

     ..
        Data flows from the input module, through the "black box"
        module, and finally into (and through) the output module.

The Emacs stanza at the bottom of this document is inside a comment.


Escaping Mechanism
------------------

reStructuredText uses backslashes ("``\``") to override the special
meaning given to markup characters and get the literal characters
themselves.  To get a literal backslash, use an escaped backslash
("``\\``").  There are two contexts in which backslashes have no
special meaning: `literal blocks`_ and inline literals (see `Inline
Markup`_ above).  In these contexts, no markup recognition is done,
and a single backslash represents a literal backslash, without having
to double up.

If you find that you need to use a backslash in your text, consider
using inline literals or a literal block instead.


Habits to Avoid
===============

Many programmers who are familiar with TeX often write quotation marks
like this::

    `single-quoted' or ``double-quoted''

Backquotes are significant in reStructuredText, so this practice
should be avoided.  For ordinary text, use ordinary 'single-quotes' or
"double-quotes".  For inline literal text (see `Inline Markup`_
above), use double-backquotes::

    ``literal text: in here, anything goes!``


Suggested Sections
==================

Various sections are found to be common across PEPs and are outlined in
:pep:`1`. Those sections are provided here for convenience.

.. _template:

.. include:: pep-0012/pep-NNNN.rst
   :literal:


Resources
=========

Many other constructs and variations are possible.  For more details
about the reStructuredText markup, in increasing order of
thoroughness, please see:

* `A ReStructuredText Primer`__, a gentle introduction.

  __ http://docutils.sourceforge.net/docs/rst/quickstart.html

* `Quick reStructuredText`__, a users' quick reference.

  __ http://docutils.sourceforge.net/docs/rst/quickref.html

* `reStructuredText Markup Specification`__, the final authority.

  __ http://docutils.sourceforge.net/spec/rst/reStructuredText.html

The processing of reStructuredText PEPs is done using Docutils_.  If
you have a question or require assistance with reStructuredText or
Docutils, please `post a message`_ to the `Docutils-users mailing
list`_.  The `Docutils project web site`_ has more information.

.. _Docutils:
.. _Docutils project web site: http://docutils.sourceforge.net/
.. _post a message:
   mailto:docutils-users@lists.sourceforge.net?subject=PEPs
.. _Docutils-users mailing list:
   http://docutils.sf.net/docs/user/mailing-lists.html#docutils-users


Copyright
=========

This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.



..
   Local Variables:
   mode: indented-text
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   coding: utf-8
   End:
````

</details>

<details><summary><b>Step 4 — revision_4</b> (3517 words)</summary>

````text
.. note::
    For those who have written a PEP before, there is a template_
    (which is included as a file in the `PEPs repository`_).

Abstract
========

This PEP provides a boilerplate or sample template for creating your
own reStructuredText PEPs.  In conjunction with the content guidelines
in :pep:`1`, this should make it easy for you to conform your own
PEPs to the format outlined below.

Note: if you are reading this PEP via the web, you should first grab
the text (reStructuredText) source of this PEP in order to complete
the steps below.  **DO NOT USE THE HTML FILE AS YOUR TEMPLATE!**

The source for this (or any) PEP can be found in the
`PEPs repository <https://github.com/python/peps/>`_,
as well as via a link at the bottom of each PEP.


Rationale
=========

If you intend to submit a PEP, you MUST use this template, in
conjunction with the format guidelines below, to ensure that your PEP
submission won't get automatically rejected because of form.

ReStructuredText provides PEP authors with useful functionality and
expressivity, while maintaining easy readability in the source text.
The processed HTML form makes the functionality accessible to readers:
live hyperlinks, styled text, tables, images, and automatic tables of
contents, among other advantages.


How to Use This Template
========================

To use this template you must first decide whether your PEP is going
to be an Informational or Standards Track PEP.  Most PEPs are
Standards Track because they propose a new feature for the Python
language or standard library.  When in doubt, read :pep:`1` for details,
or open a tracker issue on the PEPs repo to ask for assistance.

Once you've decided which type of PEP yours is going to be, follow the
directions below.

- Make a copy of this file (the ``.rst`` file, **not** the HTML!) and
  perform the following edits. Name the new file ``pep-9999.rst`` if
  you don't yet have a PEP number assignment, or ``pep-NNNN.rst`` if
  you do. Those with push permissions are welcome to claim the next
  available number (ignoring the special blocks 3000 and 8000, and a
  handful of special allocations - currently 666, 754, and 801) and
  push it directly.

- Replace the "PEP: 12" header with "PEP: 9999" or "PEP: NNNN",
  matching the file name. Note that the file name should be padded with
  zeros (eg ``pep-0012.rst``), but the header should not (``PEP: 12``).

- Change the Title header to the title of your PEP.

- Change the Author header to include your name, and optionally your
  email address.  Be sure to follow the format carefully: your name
  must appear first, and it must not be contained in parentheses.
  Your email address may appear second (or it can be omitted) and if
  it appears, it must appear in angle brackets.  It is okay to
  obfuscate your email address.

- If none of the authors are Python core developers, include a Sponsor
  header with the name of the core developer sponsoring your PEP.

- For many PEPs, discussions will take place on python-ideas@python.org
  and/or python-dev@python.org. If there is another mailing list or
  public forum more appropriate for discussion of your new feature,
  add a Discussions-To header right after the Author header. Most
  Informational PEPs don't need a Discussions-To header.

- Change the Status header to "Draft".

- For Standards Track PEPs, change the Type header to "Standards
  Track".

- For Informational PEPs, change the Type header to "Informational".

- For Standards Track PEPs, if your feature depends on the acceptance
  of some other currently in-development PEP, add a Requires header
  right after the Type header.  The value should be the PEP number of
  the PEP yours depends on.  Don't add this header if your dependent
  feature is described in a Final PEP.

- Change the Created header to today's date.  Be sure to follow the
  format carefully: it must be in ``dd-mmm-yyyy`` format, where the
  ``mmm`` is the 3 English letter month abbreviation, i.e. one of Jan,
  Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec.

- For Standards Track PEPs, after the Created header, add a
  Python-Version header and set the value to the next planned version
  of Python, i.e. the one your new feature will hopefully make its
  first appearance in.  Do not use an alpha or beta release
  designation here.  Thus, if the last version of Python was 2.2 alpha
  1 and you're hoping to get your new feature into Python 2.2, set the
  header to::

      Python-Version: 2.2

- Leave Post-History alone for now; you'll add dates to this header
  each time you post your PEP to the designated discussion forum (see
  the Discussions-To header above). If you posted your PEP to the lists
  on August 14, 2001 and September 3, 2001, the Post-History header
  would look like::

      Post-History: 14-Aug-2001, 03-Sept-2001

  You must manually add new dates and commit them (with a pull request
  if you don't have push privileges).

- Add a Replaces header if your PEP obsoletes an earlier PEP.  The
  value of this header is the number of the PEP that your new PEP is
  replacing.  Only add this header if the older PEP is in "final"
  form, i.e. is either Accepted, Final, or Rejected.  You aren't
  replacing an older open PEP if you're submitting a competing idea.

- Now write your Abstract, Rationale, and other content for your PEP,
  replacing all this gobbledygook with your own text. Be sure to
  adhere to the format guidelines below, specifically on the
  prohibition of tab characters and the indentation requirements.
  See "Suggested Sections" below for a template of sections to include.

- Update your Footnotes section, listing any footnotes and
  non-inline link targets referenced by the text.

- Leave the Emacs stanza at the end of this file alone, including the
  formfeed character ("^L", or ``\f``).

- Create a pull request against the https://github.com/python/peps
  repository.

For reference, here are all of the possible header fields (everything
in brackets should either be replaced or have the field removed if
it has a leading ``*`` marking it as optional and it does not apply to
your PEP)::

  PEP: [NNN]
  Title: [...]
  Author: [Full Name <email at example.com>]
  Sponsor: *[Full Name <email at example.com>]
  PEP-Delegate:
  Discussions-To: *[...]
  Status: Draft
  Type: [Standards Track | Informational | Process]
  Content-Type: text/x-rst
  Requires: *[NNN]
  Created: [DD-MMM-YYYY]
  Python-Version: *[M.N]
  Post-History: [DD-MMM-YYYY]
  Replaces: *[NNN]
  Superseded-By: *[NNN]
  Resolution:


ReStructuredText PEP Formatting Requirements
============================================

The following is a PEP-specific summary of reStructuredText syntax.
For the sake of simplicity and brevity, much detail is omitted.  For
more detail, see `Resources`_ below.  `Literal blocks`_ (in which no
markup processing is done) are used for examples throughout, to
illustrate the plaintext markup.


General
-------

You must adhere to the Emacs convention of adding two spaces at the
end of every sentence.  You should fill your paragraphs to column 70,
but under no circumstances should your lines extend past column 79.
If your code samples spill over column 79, you should rewrite them.

Tab characters must never appear in the document at all.  A PEP should
include the standard Emacs stanza included by example at the bottom of
this PEP.


Section Headings
----------------

PEP headings must begin in column zero and the initial letter of each
word must be capitalized as in book titles.  Acronyms should be in all
capitals.  Section titles must be adorned with an underline, a single
repeated punctuation character, which begins in column zero and must
extend at least as far as the right edge of the title text (4
characters minimum).  First-level section titles are underlined with
"=" (equals signs), second-level section titles with "-" (hyphens),
and third-level section titles with "'" (single quotes or
apostrophes).  For example::

    First-Level Title
    =================

    Second-Level Title
    ------------------

    Third-Level Title
    '''''''''''''''''

If there are more than three levels of sections in your PEP, you may
insert overline/underline-adorned titles for the first and second
levels as follows::

    ============================
    First-Level Title (optional)
    ============================

    -----------------------------
    Second-Level Title (optional)
    -----------------------------

    Third-Level Title
    =================

    Fourth-Level Title
    ------------------

    Fifth-Level Title
    '''''''''''''''''

You shouldn't have more than five levels of sections in your PEP.  If
you do, you should consider rewriting it.

You must use two blank lines between the last line of a section's body
and the next section heading.  If a subsection heading immediately
follows a section heading, a single blank line in-between is
sufficient.

The body of each section is not normally indented, although some
constructs do use indentation, as described below.  Blank lines are
used to separate constructs.


Paragraphs
----------

Paragraphs are left-aligned text blocks separated by blank lines.
Paragraphs are not indented unless they are part of an indented
construct (such as a block quote or a list item).


Inline Markup
-------------

Portions of text within paragraphs and other text blocks may be
styled.  For example::

    Text may be marked as *emphasized* (single asterisk markup,
    typically shown in italics) or **strongly emphasized** (double
    asterisks, typically boldface).  ``Inline literals`` (using double
    backquotes) are typically rendered in a monospaced typeface.  No
    further markup recognition is done within the double backquotes,
    so they're safe for any kind of code snippets.


Block Quotes
------------

Block quotes consist of indented body elements.  For example::

    This is a paragraph.

        This is a block quote.

        A block quote may contain many paragraphs.

Block quotes are used to quote extended passages from other sources.
Block quotes may be nested inside other body elements.  Use 4 spaces
per indent level.


Literal Blocks
--------------

..
    In the text below, double backquotes are used to denote inline
    literals.  "``::``" is written so that the colons will appear in a
    monospaced font; the backquotes (``) are markup, not part of the
    text.  See "Inline Markup" above.

    By the way, this is a comment, described in "Comments" below.

Literal blocks are used for code samples or preformatted ASCII art. To
indicate a literal block, preface the indented text block with
"``::``" (two colons).  The literal block continues until the end of
the indentation.  Indent the text block by 4 spaces.  For example::

    This is a typical paragraph.  A literal block follows.

    ::

        for a in [5,4,3,2,1]:   # this is program code, shown as-is
            print a
        print "it's..."
        # a literal block continues until the indentation ends

The paragraph containing only "``::``" will be completely removed from
the output; no empty paragraph will remain.  "``::``" is also
recognized at the end of any paragraph.  If immediately preceded by
whitespace, both colons will be removed from the output.  When text
immediately precedes the "``::``", *one* colon will be removed from
the output, leaving only one colon visible (i.e., "``::``" will be
replaced by "``:``").  For example, one colon will remain visible
here::

    Paragraph::

        Literal block


Lists
-----

Bullet list items begin with one of "-", "*", or "+" (hyphen,
asterisk, or plus sign), followed by whitespace and the list item
body.  List item bodies must be left-aligned and indented relative to
the bullet; the text immediately after the bullet determines the
indentation.  For example::

    This paragraph is followed by a list.

    * This is the first bullet list item.  The blank line above the
      first list item is required; blank lines between list items
      (such as below this paragraph) are optional.

    * This is the first paragraph in the second item in the list.

      This is the second paragraph in the second item in the list.
      The blank line above this paragraph is required.  The left edge
      of this paragraph lines up with the paragraph above, both
      indented relative to the bullet.

      - This is a sublist.  The bullet lines up with the left edge of
        the text blocks above.  A sublist is a new list so requires a
        blank line above and below.

    * This is the third item of the main list.

    This paragraph is not part of the list.

Enumerated (numbered) list items are similar, but use an enumerator
instead of a bullet.  Enumerators are numbers (1, 2, 3, ...), letters
(A, B, C, ...; uppercase or lowercase), or Roman numerals (i, ii, iii,
iv, ...; uppercase or lowercase), formatted with a period suffix
("1.", "2."), parentheses ("(1)", "(2)"), or a right-parenthesis
suffix ("1)", "2)").  For example::

    1. As with bullet list items, the left edge of paragraphs must
       align.

    2. Each list item may contain multiple paragraphs, sublists, etc.

       This is the second paragraph of the second list item.

       a) Enumerated lists may be nested.
       b) Blank lines may be omitted between list items.

Definition lists are written like this::

    what
        Definition lists associate a term with a definition.

    how
        The term is a one-line phrase, and the definition is one
        or more paragraphs or body elements, indented relative to
        the term.


Tables
------

Simple tables are easy and compact::

    =====  =====  =======
      A      B    A and B
    =====  =====  =======
    False  False  False
    True   False  False
    False  True   False
    True   True   True
    =====  =====  =======

There must be at least two columns in a table (to differentiate from
section titles).  Column spans use underlines of hyphens ("Inputs"
spans the first two columns)::

    =====  =====  ======
       Inputs     Output
    ------------  ------
      A      B    A or B
    =====  =====  ======
    False  False  False
    True   False  True
    False  True   True
    True   True   True
    =====  =====  ======

Text in a first-column cell starts a new row.  No text in the first
column indicates a continuation line; the rest of the cells may
consist of multiple lines.  For example::

    =====  =========================
    col 1  col 2
    =====  =========================
    1      Second column of row 1.
    2      Second column of row 2.
           Second line of paragraph.
    3      - Second column of row 3.

           - Second item in bullet
             list (row 3, column 2).
    =====  =========================


Hyperlinks
----------

When referencing an external web page in the body of a PEP, you should
include the title of the page or a suitable description in the text, with
either an inline hyperlink or a separate explicit target with the URL.
Do not include bare URLs in the body text of the PEP, and use HTTPS
links wherever available.

Hyperlink references use backquotes and a trailing underscore to mark
up the reference text; backquotes are optional if the reference text
is a single word.  For example, to reference a hyperlink target named
``Python website``, you would write:

.. code-block:: rst

    In this paragraph, we refer to the `Python website`_.

If you intend to only reference a link once, and want to define it inline
with the text, insert the link into angle brackets (``<>``) after the text
you want to link, but before the closing backtick, with a space between the
text and the opening backtick. You should also use a double-underscore after
the closing backtick instead of a single one, which makes it an anonymous
reference to avoid conflicting with other target names. For example:

.. code-block:: rst

    Visit the `website <https://www.python.org/>`__ for more.

If you want to use one link multiple places with different linked text,
or want to ensure you don't have to update your link target names when
changing the linked text, include the target name within angle brackets
following the text to link, *with an underscore after the target name
but before the closing angle bracket* (or the link **will not work**).
For example:

.. code-block:: rst

    For further examples, see the `documentation <pydocs_>`_.

An explicit target provides the URL.  Put targets in the Footnotes section
at the end of the PEP, or immediately after the paragraph with the reference.
Hyperlink targets begin with two periods and a space (the "explicit
markup start"), followed by a leading underscore, the reference text,
a colon, and the URL.

.. code-block:: rst

    .. _Python web site: https://www.python.org/
    .. _pydocs: https://docs.python.org/

The reference text and the target text must match (although the match
is case-insensitive and ignores differences in whitespace).  Note that
the underscore trails the reference text but precedes the target text.
If you think of the underscore as a right-pointing arrow, it points
*away* from the reference and *toward* the target.


Internal and PEP/RFC Links
--------------------------

The same mechanism as hyperlinks can be used for internal references.
Every unique section title implicitly defines an internal hyperlink target.
We can make a link to the Abstract section like this:

.. code-block:: rst

    Here is a hyperlink reference to the `Abstract`_ section.  The
    backquotes are optional since the reference text is a single word;
    we can also just write: Abstract_.

To refer to PEPs or RFCs, always use the ``:pep:`` and ``:rfc:`` roles,
never hardcoded URLs.
For example:

.. code-block:: rst

    See :pep:`1` for more information on how to write a PEP,
    and :pep:`the Hyperlink section of PEP 12 <12#hyperlinks>` for how to link.

This renders as:

    See :pep:`1` for more information on how to write a PEP,
    and :pep:`the Hyperlink section of PEP 12 <12#hyperlinks>` for how to link.

PEP numbers in the text are never padded, and there is a space (not a dash)
between "PEP" or "RFC" and the number; the above roles will take care of
that for you.


Footnotes
---------

Footnote references consist of a left square bracket, a label, a
right square bracket, and a trailing underscore.
Instead of a number, use a label of the
form "#word", where "word" is a mnemonic consisting of alphanumerics
plus internal hyphens, underscores, and periods (no whitespace or
other characters are allowed).
For example:

.. code-block:: rst

    Refer to The TeXbook [#TeXbook]_ for more information.

which renders as

    Refer to The TeXbook [#TeXbook]_ for more information.

Whitespace must precede the footnote reference.  Leave a space between
the footnote reference and the preceding word.

Use footnotes for additional notes, explanations and caveats, as well as
for references to books and other sources not readily available online.
Native reST hyperlink targets or inline hyperlinks in the text should be
used in preference to footnotes for including URLs to online resources.

Footnotes begin with ".. " (the explicit
markup start), followed by the footnote marker (no underscores),
followed by the footnote body.  For example:

.. code-block:: rst

    .. [#TeXbook] Donald Knuth's *The TeXbook*, pages 195 and 196.

which renders as

    .. [#TeXbook] Donald Knuth's *The TeXbook*, pages 195 and 196.

Footnotes and footnote references will be numbered automatically, and
the numbers will always match.


Images
------

If your PEP contains a diagram, you may include it in the processed
output using the "image" directive::

    .. image:: diagram.png

Any browser-friendly graphics format is possible: .png, .jpeg, .gif,
.tiff, etc.

Since this image will not be visible to readers of the PEP in source
text form, you should consider including a description or ASCII art
alternative, using a comment (below).


Comments
--------

A comment block is an indented block of arbitrary text immediately
following an explicit markup start: two periods and whitespace.  Leave
the ".." on a line by itself to ensure that the comment is not
misinterpreted as another explicit markup construct.  Comments are not
visible in the processed document.  For the benefit of those reading
your PEP in source form, please consider including a descriptions of
or ASCII art alternatives to any images you include.  For example::

     .. image:: dataflow.png

     ..
        Data flows from the input module, through the "black box"
        module, and finally into (and through) the output module.

The Emacs stanza at the bottom of this document is inside a comment.


Escaping Mechanism
------------------

reStructuredText uses backslashes ("``\``") to override the special
meaning given to markup characters and get the literal characters
themselves.  To get a literal backslash, use an escaped backslash
("``\\``").  There are two contexts in which backslashes have no
special meaning: `literal blocks`_ and inline literals (see `Inline
Markup`_ above).  In these contexts, no markup recognition is done,
and a single backslash represents a literal backslash, without having
to double up.

If you find that you need to use a backslash in your text, consider
using inline literals or a literal block instead.


Habits to Avoid
===============

Many programmers who are familiar with TeX often write quotation marks
like this::

    `single-quoted' or ``double-quoted''

Backquotes are significant in reStructuredText, so this practice
should be avoided.  For ordinary text, use ordinary 'single-quotes' or
"double-quotes".  For inline literal text (see `Inline Markup`_
above), use double-backquotes::

    ``literal text: in here, anything goes!``


Suggested Sections
==================

Various sections are found to be common across PEPs and are outlined in
:pep:`1`. Those sections are provided here for convenience.

.. _template:

.. include:: pep-0012/pep-NNNN.rst
   :literal:


Resources
=========

Many other constructs and variations are possible.  For more details
about the reStructuredText markup, in increasing order of
thoroughness, please see:

* `A ReStructuredText Primer`__, a gentle introduction.

  __ https://docutils.sourceforge.io/docs/user/rst/quickstart.html

* `Quick reStructuredText`__, a users' quick reference.

  __ https://docutils.sourceforge.io/docs/user/rst/quickref.html

* `reStructuredText Markup Specification`__, the final authority.

  __ https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html

The processing of reStructuredText PEPs is done using Docutils_.  If
you have a question or require assistance with reStructuredText or
Docutils, please `post a message`_ to the `Docutils-users mailing
list`_.  The `Docutils project web site`_ has more information.

.. _Docutils:
.. _Docutils project web site: https://docutils.sourceforge.io/
.. _post a message:
   mailto:docutils-users@lists.sourceforge.net?subject=PEPs
.. _Docutils-users mailing list:
   https://docutils.sourceforge.io/docs/user/mailing-lists.html#docutils-users


Copyright
=========

This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.



..
   Local Variables:
   mode: indented-text
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   coding: utf-8
   End:
````

</details>

<details><summary><b>Step 5 — revision_5</b> (3481 words)</summary>

````text
.. note::
    For those who have written a PEP before, there is a template_
    (which is included as a file in the `PEPs repository`_).

Abstract
========

This PEP provides a boilerplate or sample template for creating your
own reStructuredText PEPs.  In conjunction with the content guidelines
in :pep:`1`, this should make it easy for you to conform your own
PEPs to the format outlined below.

Note: if you are reading this PEP via the web, you should first grab
the text (reStructuredText) source of this PEP in order to complete
the steps below.  **DO NOT USE THE HTML FILE AS YOUR TEMPLATE!**

The source for this (or any) PEP can be found in the
`PEPs repository <https://github.com/python/peps/>`_,
as well as via a link at the bottom of each PEP.


Rationale
=========

If you intend to submit a PEP, you MUST use this template, in
conjunction with the format guidelines below, to ensure that your PEP
submission won't get automatically rejected because of form.

ReStructuredText provides PEP authors with useful functionality and
expressivity, while maintaining easy readability in the source text.
The processed HTML form makes the functionality accessible to readers:
live hyperlinks, styled text, tables, images, and automatic tables of
contents, among other advantages.


How to Use This Template
========================

To use this template you must first decide whether your PEP is going
to be an Informational or Standards Track PEP.  Most PEPs are
Standards Track because they propose a new feature for the Python
language or standard library.  When in doubt, read :pep:`1` for details,
or open a tracker issue on the PEPs repo to ask for assistance.

Once you've decided which type of PEP yours is going to be, follow the
directions below.

- Make a copy of this file (the ``.rst`` file, **not** the HTML!) and
  perform the following edits. Name the new file ``pep-9999.rst`` if
  you don't yet have a PEP number assignment, or ``pep-NNNN.rst`` if
  you do. Those with push permissions are welcome to claim the next
  available number (ignoring the special blocks 3000 and 8000, and a
  handful of special allocations - currently 666, 754, and 801) and
  push it directly.

- Replace the "PEP: 12" header with "PEP: 9999" or "PEP: NNNN",
  matching the file name. Note that the file name should be padded with
  zeros (eg ``pep-0012.rst``), but the header should not (``PEP: 12``).

- Change the Title header to the title of your PEP.

- Change the Author header to include your name, and optionally your
  email address.  Be sure to follow the format carefully: your name
  must appear first, and it must not be contained in parentheses.
  Your email address may appear second (or it can be omitted) and if
  it appears, it must appear in angle brackets.  It is okay to
  obfuscate your email address.

- If none of the authors are Python core developers, include a Sponsor
  header with the name of the core developer sponsoring your PEP.

- Add the direct URL of the PEP's canonical discussion thread
  (on e.g. Python-Dev, Discourse, etc) under the Discussions-To header.
  If the thread will be created after the PEP is submitted as an official
  draft, it is okay to just list the venue name initially, but remember to
  update the PEP with the URL as soon as the PEP is successfully merged
  to the PEPs repository and you create the corresponding discussion thread.
  See :pep:`PEP 1 <1#discussing-a-pep>` for more details.

- Change the Status header to "Draft".

- For Standards Track PEPs, change the Type header to "Standards
  Track".

- For Informational PEPs, change the Type header to "Informational".

- For Standards Track PEPs, if your feature depends on the acceptance
  of some other currently in-development PEP, add a Requires header
  right after the Type header.  The value should be the PEP number of
  the PEP yours depends on.  Don't add this header if your dependent
  feature is described in a Final PEP.

- Change the Created header to today's date.  Be sure to follow the
  format carefully: it must be in ``dd-mmm-yyyy`` format, where the
  ``mmm`` is the 3 English letter month abbreviation, i.e. one of Jan,
  Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec.

- For Standards Track PEPs, after the Created header, add a
  Python-Version header and set the value to the next planned version
  of Python, i.e. the one your new feature will hopefully make its
  first appearance in.  Do not use an alpha or beta release
  designation here.  Thus, if the last version of Python was 2.2 alpha
  1 and you're hoping to get your new feature into Python 2.2, set the
  header to::

      Python-Version: 2.2

- Leave Post-History alone for now; you'll add dates to this header
  each time you post your PEP to the designated discussion forum (and announce
  it on Python-Dev, if needed; see the ``Discussions-To`` header above).
  If you posted threads for your PEP on August 14, 2001 and September 3, 2001,
  the Post-History header would look like::

      Post-History: 14-Aug-2001, 03-Sept-2001

  You must manually add new dates and commit them (with a pull request
  if you don't have push privileges).

- Add a Replaces header if your PEP obsoletes an earlier PEP.  The
  value of this header is the number of the PEP that your new PEP is
  replacing.  Only add this header if the older PEP is in "final"
  form, i.e. is either Accepted, Final, or Rejected.  You aren't
  replacing an older open PEP if you're submitting a competing idea.

- Now write your Abstract, Rationale, and other content for your PEP,
  replacing all this gobbledygook with your own text. Be sure to
  adhere to the format guidelines below, specifically on the
  prohibition of tab characters and the indentation requirements.
  See "Suggested Sections" below for a template of sections to include.

- Update your Footnotes section, listing any footnotes and
  non-inline link targets referenced by the text.

- Create a pull request against the https://github.com/python/peps
  repository.

For reference, here are all of the possible header fields (everything
in brackets should either be replaced or have the field removed if
it has a leading ``*`` marking it as optional and it does not apply to
your PEP)::

  PEP: [NNN]
  Title: [...]
  Author: [Full Name <email at example.com>]
  Sponsor: *[Full Name <email at example.com>]
  PEP-Delegate:
  Discussions-To: [URL]
  Status: Draft
  Type: [Standards Track | Informational | Process]
  Content-Type: text/x-rst
  Requires: *[NNN]
  Created: [DD-MMM-YYYY]
  Python-Version: *[M.N]
  Post-History: [DD-MMM-YYYY]
  Replaces: *[NNN]
  Superseded-By: *[NNN]
  Resolution:


ReStructuredText PEP Formatting Requirements
============================================

The following is a PEP-specific summary of reStructuredText syntax.
For the sake of simplicity and brevity, much detail is omitted.  For
more detail, see `Resources`_ below.  `Literal blocks`_ (in which no
markup processing is done) are used for examples throughout, to
illustrate the plaintext markup.


General
-------

Lines should usually not extend past column 79,
excepting URLs and similar circumstances.
Tab characters must never appear in the document at all.


Section Headings
----------------

PEP headings must begin in column zero and the initial letter of each
word must be capitalized as in book titles.  Acronyms should be in all
capitals.  Section titles must be adorned with an underline, a single
repeated punctuation character, which begins in column zero and must
extend at least as far as the right edge of the title text (4
characters minimum).  First-level section titles are underlined with
"=" (equals signs), second-level section titles with "-" (hyphens),
and third-level section titles with "'" (single quotes or
apostrophes).  For example::

    First-Level Title
    =================

    Second-Level Title
    ------------------

    Third-Level Title
    '''''''''''''''''

If there are more than three levels of sections in your PEP, you may
insert overline/underline-adorned titles for the first and second
levels as follows::

    ============================
    First-Level Title (optional)
    ============================

    -----------------------------
    Second-Level Title (optional)
    -----------------------------

    Third-Level Title
    =================

    Fourth-Level Title
    ------------------

    Fifth-Level Title
    '''''''''''''''''

You shouldn't have more than five levels of sections in your PEP.  If
you do, you should consider rewriting it.

You must use two blank lines between the last line of a section's body
and the next section heading.  If a subsection heading immediately
follows a section heading, a single blank line in-between is
sufficient.

The body of each section is not normally indented, although some
constructs do use indentation, as described below.  Blank lines are
used to separate constructs.


Paragraphs
----------

Paragraphs are left-aligned text blocks separated by blank lines.
Paragraphs are not indented unless they are part of an indented
construct (such as a block quote or a list item).


Inline Markup
-------------

Portions of text within paragraphs and other text blocks may be
styled.  For example::

    Text may be marked as *emphasized* (single asterisk markup,
    typically shown in italics) or **strongly emphasized** (double
    asterisks, typically boldface).  ``Inline literals`` (using double
    backquotes) are typically rendered in a monospaced typeface.  No
    further markup recognition is done within the double backquotes,
    so they're safe for any kind of code snippets.


Block Quotes
------------

Block quotes consist of indented body elements.  For example::

    This is a paragraph.

        This is a block quote.

        A block quote may contain many paragraphs.

Block quotes are used to quote extended passages from other sources.
Block quotes may be nested inside other body elements.  Use 4 spaces
per indent level.


Literal Blocks
--------------

..
    In the text below, double backquotes are used to denote inline
    literals.  "``::``" is written so that the colons will appear in a
    monospaced font; the backquotes (``) are markup, not part of the
    text.  See "Inline Markup" above.

    By the way, this is a comment, described in "Comments" below.

Literal blocks are used for code samples or preformatted ASCII art. To
indicate a literal block, preface the indented text block with
"``::``" (two colons).  The literal block continues until the end of
the indentation.  Indent the text block by 4 spaces.  For example::

    This is a typical paragraph.  A literal block follows.

    ::

        for a in [5,4,3,2,1]:   # this is program code, shown as-is
            print a
        print "it's..."
        # a literal block continues until the indentation ends

The paragraph containing only "``::``" will be completely removed from
the output; no empty paragraph will remain.  "``::``" is also
recognized at the end of any paragraph.  If immediately preceded by
whitespace, both colons will be removed from the output.  When text
immediately precedes the "``::``", *one* colon will be removed from
the output, leaving only one colon visible (i.e., "``::``" will be
replaced by "``:``").  For example, one colon will remain visible
here::

    Paragraph::

        Literal block


Lists
-----

Bullet list items begin with one of "-", "*", or "+" (hyphen,
asterisk, or plus sign), followed by whitespace and the list item
body.  List item bodies must be left-aligned and indented relative to
the bullet; the text immediately after the bullet determines the
indentation.  For example::

    This paragraph is followed by a list.

    * This is the first bullet list item.  The blank line above the
      first list item is required; blank lines between list items
      (such as below this paragraph) are optional.

    * This is the first paragraph in the second item in the list.

      This is the second paragraph in the second item in the list.
      The blank line above this paragraph is required.  The left edge
      of this paragraph lines up with the paragraph above, both
      indented relative to the bullet.

      - This is a sublist.  The bullet lines up with the left edge of
        the text blocks above.  A sublist is a new list so requires a
        blank line above and below.

    * This is the third item of the main list.

    This paragraph is not part of the list.

Enumerated (numbered) list items are similar, but use an enumerator
instead of a bullet.  Enumerators are numbers (1, 2, 3, ...), letters
(A, B, C, ...; uppercase or lowercase), or Roman numerals (i, ii, iii,
iv, ...; uppercase or lowercase), formatted with a period suffix
("1.", "2."), parentheses ("(1)", "(2)"), or a right-parenthesis
suffix ("1)", "2)").  For example::

    1. As with bullet list items, the left edge of paragraphs must
       align.

    2. Each list item may contain multiple paragraphs, sublists, etc.

       This is the second paragraph of the second list item.

       a) Enumerated lists may be nested.
       b) Blank lines may be omitted between list items.

Definition lists are written like this::

    what
        Definition lists associate a term with a definition.

    how
        The term is a one-line phrase, and the definition is one
        or more paragraphs or body elements, indented relative to
        the term.


Tables
------

Simple tables are easy and compact::

    =====  =====  =======
      A      B    A and B
    =====  =====  =======
    False  False  False
    True   False  False
    False  True   False
    True   True   True
    =====  =====  =======

There must be at least two columns in a table (to differentiate from
section titles).  Column spans use underlines of hyphens ("Inputs"
spans the first two columns)::

    =====  =====  ======
       Inputs     Output
    ------------  ------
      A      B    A or B
    =====  =====  ======
    False  False  False
    True   False  True
    False  True   True
    True   True   True
    =====  =====  ======

Text in a first-column cell starts a new row.  No text in the first
column indicates a continuation line; the rest of the cells may
consist of multiple lines.  For example::

    =====  =========================
    col 1  col 2
    =====  =========================
    1      Second column of row 1.
    2      Second column of row 2.
           Second line of paragraph.
    3      - Second column of row 3.

           - Second item in bullet
             list (row 3, column 2).
    =====  =========================


Hyperlinks
----------

When referencing an external web page in the body of a PEP, you should
include the title of the page or a suitable description in the text, with
either an inline hyperlink or a separate explicit target with the URL.
Do not include bare URLs in the body text of the PEP, and use HTTPS
links wherever available.

Hyperlink references use backquotes and a trailing underscore to mark
up the reference text; backquotes are optional if the reference text
is a single word.  For example, to reference a hyperlink target named
``Python website``, you would write:

.. code-block:: rst

    In this paragraph, we refer to the `Python website`_.

If you intend to only reference a link once, and want to define it inline
with the text, insert the link into angle brackets (``<>``) after the text
you want to link, but before the closing backtick, with a space between the
text and the opening backtick. You should also use a double-underscore after
the closing backtick instead of a single one, which makes it an anonymous
reference to avoid conflicting with other target names. For example:

.. code-block:: rst

    Visit the `website <https://www.python.org/>`__ for more.

If you want to use one link multiple places with different linked text,
or want to ensure you don't have to update your link target names when
changing the linked text, include the target name within angle brackets
following the text to link, *with an underscore after the target name
but before the closing angle bracket* (or the link **will not work**).
For example:

.. code-block:: rst

    For further examples, see the `documentation <pydocs_>`_.

An explicit target provides the URL.  Put targets in the Footnotes section
at the end of the PEP, or immediately after the paragraph with the reference.
Hyperlink targets begin with two periods and a space (the "explicit
markup start"), followed by a leading underscore, the reference text,
a colon, and the URL.

.. code-block:: rst

    .. _Python web site: https://www.python.org/
    .. _pydocs: https://docs.python.org/

The reference text and the target text must match (although the match
is case-insensitive and ignores differences in whitespace).  Note that
the underscore trails the reference text but precedes the target text.
If you think of the underscore as a right-pointing arrow, it points
*away* from the reference and *toward* the target.


Internal and PEP/RFC Links
--------------------------

The same mechanism as hyperlinks can be used for internal references.
Every unique section title implicitly defines an internal hyperlink target.
We can make a link to the Abstract section like this:

.. code-block:: rst

    Here is a hyperlink reference to the `Abstract`_ section.  The
    backquotes are optional since the reference text is a single word;
    we can also just write: Abstract_.

To refer to PEPs or RFCs, always use the ``:pep:`` and ``:rfc:`` roles,
never hardcoded URLs.
For example:

.. code-block:: rst

    See :pep:`1` for more information on how to write a PEP,
    and :pep:`the Hyperlink section of PEP 12 <12#hyperlinks>` for how to link.

This renders as:

    See :pep:`1` for more information on how to write a PEP,
    and :pep:`the Hyperlink section of PEP 12 <12#hyperlinks>` for how to link.

PEP numbers in the text are never padded, and there is a space (not a dash)
between "PEP" or "RFC" and the number; the above roles will take care of
that for you.


Footnotes
---------

Footnote references consist of a left square bracket, a label, a
right square bracket, and a trailing underscore.
Instead of a number, use a label of the
form "#word", where "word" is a mnemonic consisting of alphanumerics
plus internal hyphens, underscores, and periods (no whitespace or
other characters are allowed).
For example:

.. code-block:: rst

    Refer to The TeXbook [#TeXbook]_ for more information.

which renders as

    Refer to The TeXbook [#TeXbook]_ for more information.

Whitespace must precede the footnote reference.  Leave a space between
the footnote reference and the preceding word.

Use footnotes for additional notes, explanations and caveats, as well as
for references to books and other sources not readily available online.
Native reST hyperlink targets or inline hyperlinks in the text should be
used in preference to footnotes for including URLs to online resources.

Footnotes begin with ".. " (the explicit
markup start), followed by the footnote marker (no underscores),
followed by the footnote body.  For example:

.. code-block:: rst

    .. [#TeXbook] Donald Knuth's *The TeXbook*, pages 195 and 196.

which renders as

    .. [#TeXbook] Donald Knuth's *The TeXbook*, pages 195 and 196.

Footnotes and footnote references will be numbered automatically, and
the numbers will always match.


Images
------

If your PEP contains a diagram or other graphic, you may include it in the
processed output using the ``image`` directive:

.. code-block:: rst

    .. image:: diagram.png

Any browser-friendly graphics format is possible; PNG should be
preferred for graphics, JPEG for photos and GIF for animations.
Currently, SVG must be avoided due to compatibility issues with the
PEP build system.

For accessibility and readers of the source text, you should include
a description of the image and any key information contained within
using the ``:alt:`` option to the ``image`` directive:

.. code-block:: rst

     .. image:: dataflow.png
        :alt: Data flows from the input module, through the "black box"
              module, and finally into (and through) the output module.


Comments
--------

A comment is an indented block of arbitrary text immediately
following an explicit markup start: two periods and whitespace.  Leave
the ".." on a line by itself to ensure that the comment is not
misinterpreted as another explicit markup construct.  Comments are not
visible in the processed document.  For example:

.. code-block:: rst

     ..
        This section should be updated in the final PEP.
        Ensure the date is accurate.


Escaping Mechanism
------------------

reStructuredText uses backslashes ("``\``") to override the special
meaning given to markup characters and get the literal characters
themselves.  To get a literal backslash, use an escaped backslash
("``\\``").  There are two contexts in which backslashes have no
special meaning: `literal blocks`_ and inline literals (see `Inline
Markup`_ above).  In these contexts, no markup recognition is done,
and a single backslash represents a literal backslash, without having
to double up.

If you find that you need to use a backslash in your text, consider
using inline literals or a literal block instead.


Habits to Avoid
===============

Many programmers who are familiar with TeX often write quotation marks
like this::

    `single-quoted' or ``double-quoted''

Backquotes are significant in reStructuredText, so this practice
should be avoided.  For ordinary text, use ordinary 'single-quotes' or
"double-quotes".  For inline literal text (see `Inline Markup`_
above), use double-backquotes::

    ``literal text: in here, anything goes!``


Suggested Sections
==================

Various sections are found to be common across PEPs and are outlined in
:pep:`1`. Those sections are provided here for convenience.

.. _template:

.. include:: pep-0012/pep-NNNN.rst
   :literal:


Resources
=========

Many other constructs and variations are possible.  For more details
about the reStructuredText markup, in increasing order of
thoroughness, please see:

* `A ReStructuredText Primer`__, a gentle introduction.

  __ https://docutils.sourceforge.io/docs/user/rst/quickstart.html

* `Quick reStructuredText`__, a users' quick reference.

  __ https://docutils.sourceforge.io/docs/user/rst/quickref.html

* `reStructuredText Markup Specification`__, the final authority.

  __ https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html

The processing of reStructuredText PEPs is done using Docutils_.  If
you have a question or require assistance with reStructuredText or
Docutils, please `post a message`_ to the `Docutils-users mailing
list`_.  The `Docutils project web site`_ has more information.

.. _Docutils:
.. _Docutils project web site: https://docutils.sourceforge.io/
.. _post a message:
   mailto:docutils-users@lists.sourceforge.net?subject=PEPs
.. _Docutils-users mailing list:
   https://docutils.sourceforge.io/docs/user/mailing-lists.html#docutils-users


Copyright
=========

This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.
````

</details>

<details><summary><b>Step 6 — revision_6</b> (3604 words)</summary>

````text
.. highlight:: rst

.. note::
    For those who have written a PEP before, there is a template_
    (which is included as a file in the `PEPs repository`_).

Abstract
========

This PEP provides a boilerplate or sample template for creating your
own reStructuredText PEPs.  In conjunction with the content guidelines
in :pep:`1`, this should make it easy for you to conform your own
PEPs to the format outlined below.

Note: if you are reading this PEP via the web, you should first grab
the text (reStructuredText) source of this PEP in order to complete
the steps below.  **DO NOT USE THE HTML FILE AS YOUR TEMPLATE!**

The source for this (or any) PEP can be found in the
`PEPs repository <https://github.com/python/peps/>`_,
as well as via a link at the bottom of each PEP.


Rationale
=========

If you intend to submit a PEP, you MUST use this template, in
conjunction with the format guidelines below, to ensure that your PEP
submission won't get automatically rejected because of form.

ReStructuredText provides PEP authors with useful functionality and
expressivity, while maintaining easy readability in the source text.
The processed HTML form makes the functionality accessible to readers:
live hyperlinks, styled text, tables, images, and automatic tables of
contents, among other advantages.


How to Use This Template
========================

To use this template you must first decide whether your PEP is going
to be an Informational or Standards Track PEP.  Most PEPs are
Standards Track because they propose a new feature for the Python
language or standard library.  When in doubt, read :pep:`1` for details,
or open a tracker issue on the PEPs repo to ask for assistance.

Once you've decided which type of PEP yours is going to be, follow the
directions below.

- Make a copy of this file (the ``.rst`` file, **not** the HTML!) and
  perform the following edits. Name the new file ``pep-9999.rst`` if
  you don't yet have a PEP number assignment, or ``pep-NNNN.rst`` if
  you do. Those with push permissions are welcome to claim the next
  available number (ignoring the special blocks 3000 and 8000, and a
  handful of special allocations - currently 666, 754, and 801) and
  push it directly.

- Replace the "PEP: 12" header with "PEP: 9999" or "PEP: NNNN",
  matching the file name. Note that the file name should be padded with
  zeros (eg ``pep-0012.rst``), but the header should not (``PEP: 12``).

- Change the Title header to the title of your PEP.

- Change the Author header to include your name, and optionally your
  email address.  Be sure to follow the format carefully: your name
  must appear first, and it must not be contained in parentheses.
  Your email address may appear second (or it can be omitted) and if
  it appears, it must appear in angle brackets.  It is okay to
  obfuscate your email address.

- If none of the authors are Python core developers, include a Sponsor
  header with the name of the core developer sponsoring your PEP.

- Add the direct URL of the PEP's canonical discussion thread
  (on e.g. Python-Dev, Discourse, etc) under the Discussions-To header.
  If the thread will be created after the PEP is submitted as an official
  draft, it is okay to just list the venue name initially, but remember to
  update the PEP with the URL as soon as the PEP is successfully merged
  to the PEPs repository and you create the corresponding discussion thread.
  See :pep:`PEP 1 <1#discussing-a-pep>` for more details.

- Change the Status header to "Draft".

- For Standards Track PEPs, change the Type header to "Standards
  Track".

- For Informational PEPs, change the Type header to "Informational".

- For Standards Track PEPs, if your feature depends on the acceptance
  of some other currently in-development PEP, add a Requires header
  right after the Type header.  The value should be the PEP number of
  the PEP yours depends on.  Don't add this header if your dependent
  feature is described in a Final PEP.

- Change the Created header to today's date.  Be sure to follow the
  format carefully: it must be in ``dd-mmm-yyyy`` format, where the
  ``mmm`` is the 3 English letter month abbreviation, i.e. one of Jan,
  Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec.

- For Standards Track PEPs, after the Created header, add a
  Python-Version header and set the value to the next planned version
  of Python, i.e. the one your new feature will hopefully make its
  first appearance in.  Do not use an alpha or beta release
  designation here.  Thus, if the last version of Python was 2.2 alpha
  1 and you're hoping to get your new feature into Python 2.2, set the
  header to:

  .. code-block:: email

      Python-Version: 2.2

- Leave Post-History alone for now; you'll add dates and corresponding links
  to this header each time you post your PEP to the designated discussion forum
  (and update the Discussions-To header with said link, as above).
  For each thread, use the date (in the ``dd-mmm-yyy`` format) as the
  linked text, and insert the URLs inline as anonymous reST `hyperlinks`_,
  with commas in between each posting.

  If you posted threads for your PEP on August 14, 2001 and September 3, 2001,
  the Post-History header would look like, e.g.:

  .. code-block:: email

      Post-History: `14-Aug-2001 <https://www.example.com/thread_1>`__,
                    `03-Sept-2001 <https://www.example.com/thread_2>`__

  You should add the new dates/links here as soon as you post a
  new discussion thread.

- Add a Replaces header if your PEP obsoletes an earlier PEP.  The
  value of this header is the number of the PEP that your new PEP is
  replacing.  Only add this header if the older PEP is in "final"
  form, i.e. is either Accepted, Final, or Rejected.  You aren't
  replacing an older open PEP if you're submitting a competing idea.

- Now write your Abstract, Rationale, and other content for your PEP,
  replacing all this gobbledygook with your own text. Be sure to
  adhere to the format guidelines below, specifically on the
  prohibition of tab characters and the indentation requirements.
  See "Suggested Sections" below for a template of sections to include.

- Update your Footnotes section, listing any footnotes and
  non-inline link targets referenced by the text.

- Create a pull request against the https://github.com/python/peps
  repository.

For reference, here are all of the possible header fields (everything
in brackets should either be replaced or have the field removed if
it has a leading ``*`` marking it as optional and it does not apply to
your PEP):

.. code-block:: email

  PEP: [NNN]
  Title: [...]
  Author: [Full Name <email at example.com>]
  Sponsor: *[Full Name <email at example.com>]
  PEP-Delegate:
  Discussions-To: [URL]
  Status: Draft
  Type: [Standards Track | Informational | Process]
  Content-Type: text/x-rst
  Requires: *[NNN]
  Created: [DD-MMM-YYYY]
  Python-Version: *[M.N]
  Post-History: [`DD-MMM-YYYY <URL>`__]
  Replaces: *[NNN]
  Superseded-By: *[NNN]
  Resolution:


ReStructuredText PEP Formatting Requirements
============================================

The following is a PEP-specific summary of reStructuredText syntax.
For the sake of simplicity and brevity, much detail is omitted.  For
more detail, see `Resources`_ below.  `Literal blocks`_ (in which no
markup processing is done) are used for examples throughout, to
illustrate the plaintext markup.


General
-------

Lines should usually not extend past column 79,
excepting URLs and similar circumstances.
Tab characters must never appear in the document at all.


Section Headings
----------------

PEP headings must begin in column zero and the initial letter of each
word must be capitalized as in book titles.  Acronyms should be in all
capitals.  Section titles must be adorned with an underline, a single
repeated punctuation character, which begins in column zero and must
extend at least as far as the right edge of the title text (4
characters minimum).  First-level section titles are underlined with
"=" (equals signs), second-level section titles with "-" (hyphens),
and third-level section titles with "'" (single quotes or
apostrophes).  For example::

    First-Level Title
    =================

    Second-Level Title
    ------------------

    Third-Level Title
    '''''''''''''''''

If there are more than three levels of sections in your PEP, you may
insert overline/underline-adorned titles for the first and second
levels as follows::

    ============================
    First-Level Title (optional)
    ============================

    -----------------------------
    Second-Level Title (optional)
    -----------------------------

    Third-Level Title
    =================

    Fourth-Level Title
    ------------------

    Fifth-Level Title
    '''''''''''''''''

You shouldn't have more than five levels of sections in your PEP.  If
you do, you should consider rewriting it.

You must use two blank lines between the last line of a section's body
and the next section heading.  If a subsection heading immediately
follows a section heading, a single blank line in-between is
sufficient.

The body of each section is not normally indented, although some
constructs do use indentation, as described below.  Blank lines are
used to separate constructs.


Paragraphs
----------

Paragraphs are left-aligned text blocks separated by blank lines.
Paragraphs are not indented unless they are part of an indented
construct (such as a block quote or a list item).


Inline Markup
-------------

Portions of text within paragraphs and other text blocks may be
styled.  For example::

    Text may be marked as *emphasized* (single asterisk markup,
    typically shown in italics) or **strongly emphasized** (double
    asterisks, typically boldface).  ``Inline literals`` (using double
    backquotes) are typically rendered in a monospaced typeface.  No
    further markup recognition is done within the double backquotes,
    so they're safe for any kind of code snippets.


Block Quotes
------------

Block quotes consist of indented body elements.  For example::

    This is a paragraph.

        This is a block quote.

        A block quote may contain many paragraphs.

Block quotes are used to quote extended passages from other sources.
Block quotes may be nested inside other body elements.  Use 4 spaces
per indent level.


Literal Blocks
--------------

..
    In the text below, double backquotes are used to denote inline
    literals.  "``::``" is written so that the colons will appear in a
    monospaced font; the backquotes (``) are markup, not part of the
    text.  See "Inline Markup" above.

    By the way, this is a comment, described in "Comments" below.

Literal blocks are used for code samples and other preformatted text.
To indicate a literal block, preface the indented text block with
"``::``" (two colons), or use the ``.. code-block::`` directive.
Indent the text block by 4 spaces; the literal block continues until the end
of the indentation. For example::

    This is a typical paragraph.  A literal block follows.

    ::

        for a in [5, 4, 3, 2, 1]:  # this is program code, shown as-is
            print(a)
        print("it's...")

"``::``" is also recognized at the end of any paragraph; if not immediately
preceded by whitespace, one colon will remain visible in the final output::

    This is an example::

        Literal block

By default, literal blocks will be syntax-highlighted as Python code.
For specific blocks that contain code or data in other languages/formats,
use the ``.. code-block:: language`` directive, substituting the "short name"
of the appropriate `Pygments lexer <https://pygments.org/docs/lexers/>`_
(or ``text`` to disable highlighting) for ``language``. For example::

    .. code-block:: rst

        An example of the ``rst`` lexer (i.e. *reStructuredText*).

For PEPs that predominantly contain literal blocks of a specific language,
use the ``.. highlight:: language`` directive with the appropriate ``language``
at the top of the PEP body (below the headers and above the Abstract).
All literal blocks will then be treated as that language,
unless specified otherwise in the specific ``.. code-block``. For example::

    .. highlight:: c

    Abstract
    ========

    Here's some C code::

        printf("Hello, World!\n");


Lists
-----

Bullet list items begin with one of "-", "*", or "+" (hyphen,
asterisk, or plus sign), followed by whitespace and the list item
body.  List item bodies must be left-aligned and indented relative to
the bullet; the text immediately after the bullet determines the
indentation.  For example::

    This paragraph is followed by a list.

    * This is the first bullet list item.  The blank line above the
      first list item is required; blank lines between list items
      (such as below this paragraph) are optional.

    * This is the first paragraph in the second item in the list.

      This is the second paragraph in the second item in the list.
      The blank line above this paragraph is required.  The left edge
      of this paragraph lines up with the paragraph above, both
      indented relative to the bullet.

      - This is a sublist.  The bullet lines up with the left edge of
        the text blocks above.  A sublist is a new list so requires a
        blank line above and below.

    * This is the third item of the main list.

    This paragraph is not part of the list.

Enumerated (numbered) list items are similar, but use an enumerator
instead of a bullet.  Enumerators are numbers (1, 2, 3, ...), letters
(A, B, C, ...; uppercase or lowercase), or Roman numerals (i, ii, iii,
iv, ...; uppercase or lowercase), formatted with a period suffix
("1.", "2."), parentheses ("(1)", "(2)"), or a right-parenthesis
suffix ("1)", "2)").  For example::

    1. As with bullet list items, the left edge of paragraphs must
       align.

    2. Each list item may contain multiple paragraphs, sublists, etc.

       This is the second paragraph of the second list item.

       a) Enumerated lists may be nested.
       b) Blank lines may be omitted between list items.

Definition lists are written like this::

    what
        Definition lists associate a term with a definition.

    how
        The term is a one-line phrase, and the definition is one
        or more paragraphs or body elements, indented relative to
        the term.


Tables
------

Simple tables are easy and compact::

    =====  =====  =======
      A      B    A and B
    =====  =====  =======
    False  False  False
    True   False  False
    False  True   False
    True   True   True
    =====  =====  =======

There must be at least two columns in a table (to differentiate from
section titles).  Column spans use underlines of hyphens ("Inputs"
spans the first two columns)::

    =====  =====  ======
       Inputs     Output
    ------------  ------
      A      B    A or B
    =====  =====  ======
    False  False  False
    True   False  True
    False  True   True
    True   True   True
    =====  =====  ======

Text in a first-column cell starts a new row.  No text in the first
column indicates a continuation line; the rest of the cells may
consist of multiple lines.  For example::

    =====  =========================
    col 1  col 2
    =====  =========================
    1      Second column of row 1.
    2      Second column of row 2.
           Second line of paragraph.
    3      - Second column of row 3.

           - Second item in bullet
             list (row 3, column 2).
    =====  =========================


Hyperlinks
----------

When referencing an external web page in the body of a PEP, you should
include the title of the page or a suitable description in the text, with
either an inline hyperlink or a separate explicit target with the URL.
Do not include bare URLs in the body text of the PEP, and use HTTPS
links wherever available.

Hyperlink references use backquotes and a trailing underscore to mark
up the reference text; backquotes are optional if the reference text
is a single word.  For example, to reference a hyperlink target named
``Python website``, you would write:

.. code-block:: rst

    In this paragraph, we refer to the `Python website`_.

If you intend to only reference a link once, and want to define it inline
with the text, insert the link into angle brackets (``<>``) after the text
you want to link, but before the closing backtick, with a space between the
text and the opening backtick. You should also use a double-underscore after
the closing backtick instead of a single one, which makes it an anonymous
reference to avoid conflicting with other target names. For example:

.. code-block:: rst

    Visit the `website <https://www.python.org/>`__ for more.

If you want to use one link multiple places with different linked text,
or want to ensure you don't have to update your link target names when
changing the linked text, include the target name within angle brackets
following the text to link, *with an underscore after the target name
but before the closing angle bracket* (or the link **will not work**).
For example:

.. code-block:: rst

    For further examples, see the `documentation <pydocs_>`_.

An explicit target provides the URL.  Put targets in the Footnotes section
at the end of the PEP, or immediately after the paragraph with the reference.
Hyperlink targets begin with two periods and a space (the "explicit
markup start"), followed by a leading underscore, the reference text,
a colon, and the URL.

.. code-block:: rst

    .. _Python web site: https://www.python.org/
    .. _pydocs: https://docs.python.org/

The reference text and the target text must match (although the match
is case-insensitive and ignores differences in whitespace).  Note that
the underscore trails the reference text but precedes the target text.
If you think of the underscore as a right-pointing arrow, it points
*away* from the reference and *toward* the target.


Internal and PEP/RFC Links
--------------------------

The same mechanism as hyperlinks can be used for internal references.
Every unique section title implicitly defines an internal hyperlink target.
We can make a link to the Abstract section like this:

.. code-block:: rst

    Here is a hyperlink reference to the `Abstract`_ section.  The
    backquotes are optional since the reference text is a single word;
    we can also just write: Abstract_.

To refer to PEPs or RFCs, always use the ``:pep:`` and ``:rfc:`` roles,
never hardcoded URLs.
For example:

.. code-block:: rst

    See :pep:`1` for more information on how to write a PEP,
    and :pep:`the Hyperlink section of PEP 12 <12#hyperlinks>` for how to link.

This renders as:

    See :pep:`1` for more information on how to write a PEP,
    and :pep:`the Hyperlink section of PEP 12 <12#hyperlinks>` for how to link.

PEP numbers in the text are never padded, and there is a space (not a dash)
between "PEP" or "RFC" and the number; the above roles will take care of
that for you.


Footnotes
---------

Footnote references consist of a left square bracket, a label, a
right square bracket, and a trailing underscore.
Instead of a number, use a label of the
form "#word", where "word" is a mnemonic consisting of alphanumerics
plus internal hyphens, underscores, and periods (no whitespace or
other characters are allowed).
For example:

.. code-block:: rst

    Refer to The TeXbook [#TeXbook]_ for more information.

which renders as

    Refer to The TeXbook [#TeXbook]_ for more information.

Whitespace must precede the footnote reference.  Leave a space between
the footnote reference and the preceding word.

Use footnotes for additional notes, explanations and caveats, as well as
for references to books and other sources not readily available online.
Native reST hyperlink targets or inline hyperlinks in the text should be
used in preference to footnotes for including URLs to online resources.

Footnotes begin with ".. " (the explicit
markup start), followed by the footnote marker (no underscores),
followed by the footnote body.  For example:

.. code-block:: rst

    .. [#TeXbook] Donald Knuth's *The TeXbook*, pages 195 and 196.

which renders as

    .. [#TeXbook] Donald Knuth's *The TeXbook*, pages 195 and 196.

Footnotes and footnote references will be numbered automatically, and
the numbers will always match.


Images
------

If your PEP contains a diagram or other graphic, you may include it in the
processed output using the ``image`` directive:

.. code-block:: rst

    .. image:: diagram.png

Any browser-friendly graphics format is possible; PNG should be
preferred for graphics, JPEG for photos and GIF for animations.
Currently, SVG must be avoided due to compatibility issues with the
PEP build system.

For accessibility and readers of the source text, you should include
a description of the image and any key information contained within
using the ``:alt:`` option to the ``image`` directive:

.. code-block:: rst

     .. image:: dataflow.png
        :alt: Data flows from the input module, through the "black box"
              module, and finally into (and through) the output module.


Comments
--------

A comment is an indented block of arbitrary text immediately
following an explicit markup start: two periods and whitespace.  Leave
the ".." on a line by itself to ensure that the comment is not
misinterpreted as another explicit markup construct.  Comments are not
visible in the processed document.  For example:

.. code-block:: rst

     ..
        This section should be updated in the final PEP.
        Ensure the date is accurate.


Escaping Mechanism
------------------

reStructuredText uses backslashes ("``\``") to override the special
meaning given to markup characters and get the literal characters
themselves.  To get a literal backslash, use an escaped backslash
("``\\``").  There are two contexts in which backslashes have no
special meaning: `literal blocks`_ and inline literals (see `Inline
Markup`_ above).  In these contexts, no markup recognition is done,
and a single backslash represents a literal backslash, without having
to double up.

If you find that you need to use a backslash in your text, consider
using inline literals or a literal block instead.


Habits to Avoid
===============

Many programmers who are familiar with TeX often write quotation marks
like this:

.. code-block:: text

    `single-quoted' or ``double-quoted''

Backquotes are significant in reStructuredText, so this practice
should be avoided.  For ordinary text, use ordinary 'single-quotes' or
"double-quotes".  For inline literal text (see `Inline Markup`_
above), use double-backquotes::

    ``literal text: in here, anything goes!``


Suggested Sections
==================

Various sections are found to be common across PEPs and are outlined in
:pep:`1`. Those sections are provided here for convenience.

.. _template:

.. include:: pep-0012/pep-NNNN.rst
   :code: rst


Resources
=========

Many other constructs and variations are possible.  For more details
about the reStructuredText markup, in increasing order of
thoroughness, please see:

* `A ReStructuredText Primer`__, a gentle introduction.

  __ https://docutils.sourceforge.io/docs/user/rst/quickstart.html

* `Quick reStructuredText`__, a users' quick reference.

  __ https://docutils.sourceforge.io/docs/user/rst/quickref.html

* `reStructuredText Markup Specification`__, the final authority.

  __ https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html

The processing of reStructuredText PEPs is done using Docutils_.  If
you have a question or require assistance with reStructuredText or
Docutils, please `post a message`_ to the `Docutils-users mailing
list`_.  The `Docutils project web site`_ has more information.

.. _Docutils:
.. _Docutils project web site: https://docutils.sourceforge.io/
.. _post a message:
   mailto:docutils-users@lists.sourceforge.net?subject=PEPs
.. _Docutils-users mailing list:
   https://docutils.sourceforge.io/docs/user/mailing-lists.html#docutils-users


Copyright
=========

This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.
````

</details>

<details><summary><b>Step 7 — revision_7</b> (3888 words)</summary>

````text
.. highlight:: rst

.. note::
    For those who have written a PEP before, there is a template_
    (which is included as a file in the `PEPs repository`_).

Abstract
========

This PEP provides a boilerplate or sample template for creating your
own reStructuredText PEPs.  In conjunction with the content guidelines
in :pep:`1`, this should make it easy for you to conform your own
PEPs to the format outlined below.

Note: if you are reading this PEP via the web, you should first grab
the text (reStructuredText) source of this PEP in order to complete
the steps below.  **DO NOT USE THE HTML FILE AS YOUR TEMPLATE!**

The source for this (or any) PEP can be found in the
`PEPs repository <https://github.com/python/peps/>`_,
as well as via a link at the bottom of each PEP.


Rationale
=========

If you intend to submit a PEP, you MUST use this template, in
conjunction with the format guidelines below, to ensure that your PEP
submission won't get automatically rejected because of form.

ReStructuredText provides PEP authors with useful functionality and
expressivity, while maintaining easy readability in the source text.
The processed HTML form makes the functionality accessible to readers:
live hyperlinks, styled text, tables, images, and automatic tables of
contents, among other advantages.


How to Use This Template
========================

To use this template you must first decide whether your PEP is going
to be an Informational or Standards Track PEP.  Most PEPs are
Standards Track because they propose a new feature for the Python
language or standard library.  When in doubt, read :pep:`1` for details,
or open a tracker issue on the PEPs repo to ask for assistance.

Once you've decided which type of PEP yours is going to be, follow the
directions below.

- Make a copy of this file (the ``.rst`` file, **not** the HTML!) and
  perform the following edits. Name the new file ``pep-9999.rst`` if
  you don't yet have a PEP number assignment, or ``pep-NNNN.rst`` if
  you do. Those with push permissions are welcome to claim the next
  available number (ignoring the special blocks 3000 and 8000, and a
  handful of special allocations - currently 666, 754, and 801) and
  push it directly.

- Replace the "PEP: 12" header with "PEP: 9999" or "PEP: NNNN",
  matching the file name. Note that the file name should be padded with
  zeros (eg ``pep-0012.rst``), but the header should not (``PEP: 12``).

- Change the Title header to the title of your PEP.

- Change the Author header to include your name, and optionally your
  email address.  Be sure to follow the format carefully: your name
  must appear first, and it must not be contained in parentheses.
  Your email address may appear second (or it can be omitted) and if
  it appears, it must appear in angle brackets.  It is okay to
  obfuscate your email address.

- If none of the authors are Python core developers, include a Sponsor
  header with the name of the core developer sponsoring your PEP.

- Add the direct URL of the PEP's canonical discussion thread
  (on e.g. Python-Dev, Discourse, etc) under the Discussions-To header.
  If the thread will be created after the PEP is submitted as an official
  draft, it is okay to just list the venue name initially, but remember to
  update the PEP with the URL as soon as the PEP is successfully merged
  to the PEPs repository and you create the corresponding discussion thread.
  See :pep:`PEP 1 <1#discussing-a-pep>` for more details.

- Change the Status header to "Draft".

- For Standards Track PEPs, change the Type header to "Standards
  Track".

- For Informational PEPs, change the Type header to "Informational".

- For Standards Track PEPs, if your feature depends on the acceptance
  of some other currently in-development PEP, add a Requires header
  right after the Type header.  The value should be the PEP number of
  the PEP yours depends on.  Don't add this header if your dependent
  feature is described in a Final PEP.

- Change the Created header to today's date.  Be sure to follow the
  format carefully: it must be in ``dd-mmm-yyyy`` format, where the
  ``mmm`` is the 3 English letter month abbreviation, i.e. one of Jan,
  Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec.

- For Standards Track PEPs, after the Created header, add a
  Python-Version header and set the value to the next planned version
  of Python, i.e. the one your new feature will hopefully make its
  first appearance in.  Do not use an alpha or beta release
  designation here.  Thus, if the last version of Python was 2.2 alpha
  1 and you're hoping to get your new feature into Python 2.2, set the
  header to:

  .. code-block:: email

      Python-Version: 2.2

- Leave Post-History alone for now; you'll add dates and corresponding links
  to this header each time you post your PEP to the designated discussion forum
  (and update the Discussions-To header with said link, as above).
  For each thread, use the date (in the ``dd-mmm-yyy`` format) as the
  linked text, and insert the URLs inline as anonymous reST `hyperlinks`_,
  with commas in between each posting.

  If you posted threads for your PEP on August 14, 2001 and September 3, 2001,
  the Post-History header would look like, e.g.:

  .. code-block:: email

      Post-History: `14-Aug-2001 <https://www.example.com/thread_1>`__,
                    `03-Sept-2001 <https://www.example.com/thread_2>`__

  You should add the new dates/links here as soon as you post a
  new discussion thread.

- Add a Replaces header if your PEP obsoletes an earlier PEP.  The
  value of this header is the number of the PEP that your new PEP is
  replacing.  Only add this header if the older PEP is in "final"
  form, i.e. is either Accepted, Final, or Rejected.  You aren't
  replacing an older open PEP if you're submitting a competing idea.

- Now write your Abstract, Rationale, and other content for your PEP,
  replacing all this gobbledygook with your own text. Be sure to
  adhere to the format guidelines below, specifically on the
  prohibition of tab characters and the indentation requirements.
  See "Suggested Sections" below for a template of sections to include.

- Update your Footnotes section, listing any footnotes and
  non-inline link targets referenced by the text.

- Run ``./build.py`` to ensure the PEP is rendered without errors,
  and check that the output in ``build/pep-9999.html`` looks as you intend.

- Create a pull request against the `PEPs repository`_.

For reference, here are all of the possible header fields (everything
in brackets should either be replaced or have the field removed if
it has a leading ``*`` marking it as optional and it does not apply to
your PEP):

.. code-block:: email

  PEP: [NNN]
  Title: [...]
  Author: [Full Name <email at example.com>]
  Sponsor: *[Full Name <email at example.com>]
  PEP-Delegate:
  Discussions-To: [URL]
  Status: Draft
  Type: [Standards Track | Informational | Process]
  Content-Type: text/x-rst
  Requires: *[NNN]
  Created: [DD-MMM-YYYY]
  Python-Version: *[M.N]
  Post-History: [`DD-MMM-YYYY <URL>`__]
  Replaces: *[NNN]
  Superseded-By: *[NNN]
  Resolution:


ReStructuredText PEP Formatting Requirements
============================================

The following is a PEP-specific summary of reStructuredText syntax.
For the sake of simplicity and brevity, much detail is omitted.  For
more detail, see `Resources`_ below.  `Literal blocks`_ (in which no
markup processing is done) are used for examples throughout, to
illustrate the plaintext markup.


General
-------

Lines should usually not extend past column 79,
excepting URLs and similar circumstances.
Tab characters must never appear in the document at all.


Section Headings
----------------

PEP headings must begin in column zero and the initial letter of each
word must be capitalized as in book titles.  Acronyms should be in all
capitals.  Section titles must be adorned with an underline, a single
repeated punctuation character, which begins in column zero and must
extend at least as far as the right edge of the title text (4
characters minimum).  First-level section titles are underlined with
"=" (equals signs), second-level section titles with "-" (hyphens),
and third-level section titles with "'" (single quotes or
apostrophes).  For example::

    First-Level Title
    =================

    Second-Level Title
    ------------------

    Third-Level Title
    '''''''''''''''''

If there are more than three levels of sections in your PEP, you may
insert overline/underline-adorned titles for the first and second
levels as follows::

    ============================
    First-Level Title (optional)
    ============================

    -----------------------------
    Second-Level Title (optional)
    -----------------------------

    Third-Level Title
    =================

    Fourth-Level Title
    ------------------

    Fifth-Level Title
    '''''''''''''''''

You shouldn't have more than five levels of sections in your PEP.  If
you do, you should consider rewriting it.

You must use two blank lines between the last line of a section's body
and the next section heading.  If a subsection heading immediately
follows a section heading, a single blank line in-between is
sufficient.

The body of each section is not normally indented, although some
constructs do use indentation, as described below.  Blank lines are
used to separate constructs.


Paragraphs
----------

Paragraphs are left-aligned text blocks separated by blank lines.
Paragraphs are not indented unless they are part of an indented
construct (such as a block quote or a list item).


Inline Markup
-------------

Portions of text within paragraphs and other text blocks may be
styled.  For example::

    Text may be marked as *emphasized* (single asterisk markup,
    typically shown in italics) or **strongly emphasized** (double
    asterisks, typically boldface).  ``Inline literals`` (using double
    backquotes) are typically rendered in a monospaced typeface.  No
    further markup recognition is done within the double backquotes,
    so they're safe for any kind of code snippets.


Block Quotes
------------

Block quotes consist of indented body elements.  For example::

    This is a paragraph.

        This is a block quote.

        A block quote may contain many paragraphs.

Block quotes are used to quote extended passages from other sources.
Block quotes may be nested inside other body elements.  Use 4 spaces
per indent level.


Literal Blocks
--------------

..
    In the text below, double backquotes are used to denote inline
    literals.  "``::``" is written so that the colons will appear in a
    monospaced font; the backquotes (``) are markup, not part of the
    text.  See "Inline Markup" above.

    By the way, this is a comment, described in "Comments" below.

Literal blocks are used for code samples and other preformatted text.
To indicate a literal block, preface the indented text block with
"``::``" (two colons), or use the ``.. code-block::`` directive.
Indent the text block by 4 spaces; the literal block continues until the end
of the indentation. For example::

    This is a typical paragraph.  A literal block follows.

    ::

        for a in [5, 4, 3, 2, 1]:  # this is program code, shown as-is
            print(a)
        print("it's...")

"``::``" is also recognized at the end of any paragraph; if not immediately
preceded by whitespace, one colon will remain visible in the final output::

    This is an example::

        Literal block

By default, literal blocks will be syntax-highlighted as Python code.
For specific blocks that contain code or data in other languages/formats,
use the ``.. code-block:: language`` directive, substituting the "short name"
of the appropriate `Pygments lexer <https://pygments.org/docs/lexers/>`_
(or ``text`` to disable highlighting) for ``language``. For example::

    .. code-block:: rst

        An example of the ``rst`` lexer (i.e. *reStructuredText*).

For PEPs that predominantly contain literal blocks of a specific language,
use the ``.. highlight:: language`` directive with the appropriate ``language``
at the top of the PEP body (below the headers and above the Abstract).
All literal blocks will then be treated as that language,
unless specified otherwise in the specific ``.. code-block``. For example::

    .. highlight:: c

    Abstract
    ========

    Here's some C code::

        printf("Hello, World!\n");


Lists
-----

Bullet list items begin with one of "-", "*", or "+" (hyphen,
asterisk, or plus sign), followed by whitespace and the list item
body.  List item bodies must be left-aligned and indented relative to
the bullet; the text immediately after the bullet determines the
indentation.  For example::

    This paragraph is followed by a list.

    * This is the first bullet list item.  The blank line above the
      first list item is required; blank lines between list items
      (such as below this paragraph) are optional.

    * This is the first paragraph in the second item in the list.

      This is the second paragraph in the second item in the list.
      The blank line above this paragraph is required.  The left edge
      of this paragraph lines up with the paragraph above, both
      indented relative to the bullet.

      - This is a sublist.  The bullet lines up with the left edge of
        the text blocks above.  A sublist is a new list so requires a
        blank line above and below.

    * This is the third item of the main list.

    This paragraph is not part of the list.

Enumerated (numbered) list items are similar, but use an enumerator
instead of a bullet.  Enumerators are numbers (1, 2, 3, ...), letters
(A, B, C, ...; uppercase or lowercase), or Roman numerals (i, ii, iii,
iv, ...; uppercase or lowercase), formatted with a period suffix
("1.", "2."), parentheses ("(1)", "(2)"), or a right-parenthesis
suffix ("1)", "2)").  For example::

    1. As with bullet list items, the left edge of paragraphs must
       align.

    2. Each list item may contain multiple paragraphs, sublists, etc.

       This is the second paragraph of the second list item.

       a) Enumerated lists may be nested.
       b) Blank lines may be omitted between list items.

Definition lists are written like this::

    what
        Definition lists associate a term with a definition.

    how
        The term is a one-line phrase, and the definition is one
        or more paragraphs or body elements, indented relative to
        the term.


Tables
------

Simple tables are easy and compact::

    =====  =====  =======
      A      B    A and B
    =====  =====  =======
    False  False  False
    True   False  False
    False  True   False
    True   True   True
    =====  =====  =======

There must be at least two columns in a table (to differentiate from
section titles).  Column spans use underlines of hyphens ("Inputs"
spans the first two columns)::

    =====  =====  ======
       Inputs     Output
    ------------  ------
      A      B    A or B
    =====  =====  ======
    False  False  False
    True   False  True
    False  True   True
    True   True   True
    =====  =====  ======

Text in a first-column cell starts a new row.  No text in the first
column indicates a continuation line; the rest of the cells may
consist of multiple lines.  For example::

    =====  =========================
    col 1  col 2
    =====  =========================
    1      Second column of row 1.
    2      Second column of row 2.
           Second line of paragraph.
    3      - Second column of row 3.

           - Second item in bullet
             list (row 3, column 2).
    =====  =========================


Hyperlinks
----------

When referencing an external web page in the body of a PEP, you should
include the title of the page or a suitable description in the text, with
either an inline hyperlink or a separate explicit target with the URL.
Do not include bare URLs in the body text of the PEP, and use HTTPS
links wherever available.

Hyperlink references use backquotes and a trailing underscore to mark
up the reference text; backquotes are optional if the reference text
is a single word.  For example, to reference a hyperlink target named
``Python website``, you would write:

.. code-block:: rst

    In this paragraph, we refer to the `Python website`_.

If you intend to only reference a link once, and want to define it inline
with the text, insert the link into angle brackets (``<>``) after the text
you want to link, but before the closing backtick, with a space between the
text and the opening backtick. You should also use a double-underscore after
the closing backtick instead of a single one, which makes it an anonymous
reference to avoid conflicting with other target names. For example:

.. code-block:: rst

    Visit the `website <https://www.python.org/>`__ for more.

If you want to use one link multiple places with different linked text,
or want to ensure you don't have to update your link target names when
changing the linked text, include the target name within angle brackets
following the text to link, *with an underscore after the target name
but before the closing angle bracket* (or the link **will not work**).
For example:

.. code-block:: rst

    For further examples, see the `documentation <pydocs_>`_.

An explicit target provides the URL.  Put targets in the Footnotes section
at the end of the PEP, or immediately after the paragraph with the reference.
Hyperlink targets begin with two periods and a space (the "explicit
markup start"), followed by a leading underscore, the reference text,
a colon, and the URL.

.. code-block:: rst

    .. _Python web site: https://www.python.org/
    .. _pydocs: https://docs.python.org/

The reference text and the target text must match (although the match
is case-insensitive and ignores differences in whitespace).  Note that
the underscore trails the reference text but precedes the target text.
If you think of the underscore as a right-pointing arrow, it points
*away* from the reference and *toward* the target.


Internal and PEP/RFC Links
--------------------------

The same mechanism as hyperlinks can be used for internal references.
Every unique section title implicitly defines an internal hyperlink target.
We can make a link to the Abstract section like this:

.. code-block:: rst

    Here is a hyperlink reference to the `Abstract`_ section.  The
    backquotes are optional since the reference text is a single word;
    we can also just write: Abstract_.

To refer to PEPs or RFCs, always use the ``:pep:`` and ``:rfc:`` roles,
never hardcoded URLs.
For example:

.. code-block:: rst

    See :pep:`1` for more information on how to write a PEP,
    and :pep:`the Hyperlink section of PEP 12 <12#hyperlinks>` for how to link.

This renders as:

    See :pep:`1` for more information on how to write a PEP,
    and :pep:`the Hyperlink section of PEP 12 <12#hyperlinks>` for how to link.

PEP numbers in the text are never padded, and there is a space (not a dash)
between "PEP" or "RFC" and the number; the above roles will take care of
that for you.


Footnotes
---------

Footnote references consist of a left square bracket, a label, a
right square bracket, and a trailing underscore.
Instead of a number, use a label of the
form "#word", where "word" is a mnemonic consisting of alphanumerics
plus internal hyphens, underscores, and periods (no whitespace or
other characters are allowed).
For example:

.. code-block:: rst

    Refer to The TeXbook [#TeXbook]_ for more information.

which renders as

    Refer to The TeXbook [#TeXbook]_ for more information.

Whitespace must precede the footnote reference.  Leave a space between
the footnote reference and the preceding word.

Use footnotes for additional notes, explanations and caveats, as well as
for references to books and other sources not readily available online.
Native reST hyperlink targets or inline hyperlinks in the text should be
used in preference to footnotes for including URLs to online resources.

Footnotes begin with ".. " (the explicit
markup start), followed by the footnote marker (no underscores),
followed by the footnote body.  For example:

.. code-block:: rst

    .. [#TeXbook] Donald Knuth's *The TeXbook*, pages 195 and 196.

which renders as

    .. [#TeXbook] Donald Knuth's *The TeXbook*, pages 195 and 196.

Footnotes and footnote references will be numbered automatically, and
the numbers will always match.


Images
------

If your PEP contains a diagram or other graphic, you may include it in the
processed output using the ``image`` directive:

.. code-block:: rst

    .. image:: diagram.png

Any browser-friendly graphics format is possible; PNG should be
preferred for graphics, JPEG for photos and GIF for animations.
Currently, SVG must be avoided due to compatibility issues with the
PEP build system.

For accessibility and readers of the source text, you should include
a description of the image and any key information contained within
using the ``:alt:`` option to the ``image`` directive:

.. code-block:: rst

     .. image:: dataflow.png
        :alt: Data flows from the input module, through the "black box"
              module, and finally into (and through) the output module.


Comments
--------

A comment is an indented block of arbitrary text immediately
following an explicit markup start: two periods and whitespace.  Leave
the ".." on a line by itself to ensure that the comment is not
misinterpreted as another explicit markup construct.  Comments are not
visible in the processed document.  For example:

.. code-block:: rst

     ..
        This section should be updated in the final PEP.
        Ensure the date is accurate.


Escaping Mechanism
------------------

reStructuredText uses backslashes ("``\``") to override the special
meaning given to markup characters and get the literal characters
themselves.  To get a literal backslash, use an escaped backslash
("``\\``").  There are two contexts in which backslashes have no
special meaning: `literal blocks`_ and inline literals (see `Inline
Markup`_ above).  In these contexts, no markup recognition is done,
and a single backslash represents a literal backslash, without having
to double up.

If you find that you need to use a backslash in your text, consider
using inline literals or a literal block instead.


Canonical Documentation and Intersphinx
---------------------------------------

As :pep:`PEP 1 describes <1#pep-maintenance>`,
PEPs are considered historical documents once marked Final,
and their canonical documentation/specification should be moved elsewhere.
To indicate this, use the ``canonical-docs`` directive
or an appropriate subclass
(currently ``canonical-pypa-spec`` for packaging standards).

Furthermore, you can use
`Intersphinx references
<https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html>`_
to other Sphinx sites,
currently the `Python documentation <https://docs.python.org/>`_
and `packaging.python.org <https://packaging.python.org/>`_,
to easily cross-reference pages, sections and Python/C objects.
This works with both the "canonical" directives and anywhere in your PEP.

Add the directive between the headers and the first section of the PEP
(typically the Abstract)
and pass as an argument an Intersphinx reference of the canonical doc/spec
(or if the target is not on a Sphinx site, a `reST hyperlink <Hyperlinks_>`__).

For example,
to create a banner pointing to the :mod:`python:sqlite3` docs,
you would write the following::

    .. canonical-doc:: :mod:`python:sqlite3`

which would generate the banner:

    .. canonical-doc:: :mod:`python:sqlite3`

Or for a PyPA spec,
such as the :ref:`packaging:core-metadata`,
you would use::

    .. canonical-pypa-spec:: :ref:`packaging:core-metadata`

which renders as:

    .. canonical-pypa-spec:: :ref:`packaging:core-metadata`

The argument accepts arbitrary reST,
so you can include multiple linked docs/specs and name them whatever you like,
and you can also include directive content that will be inserted into the text.
The following advanced example::

    .. canonical-doc:: the :ref:`python:sqlite3-connection-objects` and :exc:`python:~sqlite3.DataError` docs

        Also, see the :ref:`Data Persistence docs <persistence>` for other examples.

would render as:

    .. canonical-doc:: the :ref:`python:sqlite3-connection-objects` and :exc:`python:sqlite3.DataError` docs

        Also, see the :ref:`Data Persistence docs <persistence>` for other examples.


Habits to Avoid
===============

Many programmers who are familiar with TeX often write quotation marks
like this:

.. code-block:: text

    `single-quoted' or ``double-quoted''

Backquotes are significant in reStructuredText, so this practice
should be avoided.  For ordinary text, use ordinary 'single-quotes' or
"double-quotes".  For inline literal text (see `Inline Markup`_
above), use double-backquotes::

    ``literal text: in here, anything goes!``


Suggested Sections
==================

Various sections are found to be common across PEPs and are outlined in
:pep:`1`. Those sections are provided here for convenience.

.. _template:

.. include:: pep-0012/pep-NNNN.rst
   :code: rst


Resources
=========

Many other constructs and variations are possible,
both those supported by basic `Docutils <https://docutils.sourceforge.io/>`_
and the extensions added by `Sphinx <https://www.sphinx-doc.org/>`_.

A number of resources are available to learn more about them:

* `Sphinx ReStructuredText Primer
  <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_,
  a gentle but fairly detailed introduction.

* `reStructuredText Markup Specification
  <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html>`_,
  the authoritative, comprehensive documentation of the basic reST syntax,
  directives, roles and more.

* `Sphinx Roles
  <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html>`_
  and `Sphinx Directives
  <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_,
  the extended constructs added by the Sphinx documentation system used to
  render the PEPs to HTML.

If you have questions or require assistance with writing a PEP that the above
resources don't address, ping ``@python/pep-editors`` on GitHub, open an
`issue on the PEPs repository <https://github.com/python/peps/issues>`_
or reach out to a PEP editor directly.


Copyright
=========

This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.
````

</details>

<details><summary><b>Step 8 — final</b> (3994 words)</summary>

````text
.. highlight:: rst

.. note::
    For those who have written a PEP before, there is a template_
    (which is included as a file in the `PEPs repository`_).

Abstract
========

This PEP provides a boilerplate or sample template for creating your
own reStructuredText PEPs.  In conjunction with the content guidelines
in :pep:`1`, this should make it easy for you to conform your own
PEPs to the format outlined below.

Note: if you are reading this PEP via the web, you should first grab
the text (reStructuredText) source of this PEP in order to complete
the steps below.  **DO NOT USE THE HTML FILE AS YOUR TEMPLATE!**

The source for this (or any) PEP can be found in the
`PEPs repository <https://github.com/python/peps/>`_,
as well as via a link at the bottom of each PEP.


Specification
=============

If you intend to submit a PEP, you MUST use this template, in
conjunction with the format guidelines below, to ensure that your PEP
submission won't get automatically rejected because of form.


Rationale
=========

ReStructuredText provides PEP authors with useful functionality and
expressivity, while maintaining easy readability in the source text.
The processed HTML form makes the functionality accessible to readers:
live hyperlinks, styled text, tables, images, and automatic tables of
contents, among other advantages.


How to Use This Template
========================

To use this template you must first decide whether your PEP is going
to be an Informational or Standards Track PEP.  Most PEPs are
Standards Track because they propose a new feature for the Python
language or standard library.  When in doubt, read :pep:`1` for details,
or open a tracker issue on the PEPs repo to ask for assistance.

Once you've decided which type of PEP yours is going to be, follow the
directions below.

- Make a copy of this file (the ``.rst`` file, **not** the HTML!) and
  perform the following edits. Name the new file :file:`pep-{NNNN}.rst`, using
  the next available number (not used by a published or in-PR PEP).

- Replace the "PEP: 12" header with "PEP: NNNN",
  matching the file name. Note that the file name should be padded with
  zeros (eg ``pep-0012.rst``), but the header should not (``PEP: 12``).

- Change the Title header to the title of your PEP.

- Change the Author header to include your name, and optionally your
  email address.  Be sure to follow the format carefully: your name
  must appear first, and it must not be contained in parentheses.
  Your email address may appear second (or it can be omitted) and if
  it appears, it must appear in angle brackets.  It is okay to
  obfuscate your email address.

- If none of the authors are Python core developers, include a Sponsor
  header with the name of the core developer sponsoring your PEP.

- Add the direct URL of the PEP's canonical discussion thread
  (on e.g. Python-Dev, Discourse, etc) under the Discussions-To header.
  If the thread will be created after the PEP is submitted as an official
  draft, it is okay to just put "Pending" initially, but remember to
  update the PEP with the URL as soon as the PEP is successfully merged
  to the PEPs repository and you create the corresponding discussion thread.
  See :pep:`PEP 1 <1#discussing-a-pep>` for more details.

- Change the Status header to "Draft".

- For Standards Track PEPs, change the Type header to "Standards
  Track".

- For Informational PEPs, change the Type header to "Informational".

- For Standards Track PEPs, if your feature depends on the acceptance
  of some other currently in-development PEP, add a Requires header
  right after the Type header.  The value should be the PEP number of
  the PEP yours depends on.  Don't add this header if your dependent
  feature is described in a Final PEP.

- Change the Created header to today's date.  Be sure to follow the
  format carefully: it must be in ``DD-MMM-YYYY`` format, where the
  ``MMM`` is the three-letter English month abbreviation, i.e. one of Jan,
  Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec.

- For Standards Track PEPs, after the Created header, add a
  Python-Version header and set the value to the next planned version
  of Python, i.e. the one your new feature will hopefully make its
  first appearance in.  Do not use an alpha or beta release
  designation here.  Thus, if the last version of Python was 2.2 alpha
  1 and you're hoping to get your new feature into Python 2.2, set the
  header to:

  .. code-block:: email

      Python-Version: 2.2

- Add a Topic header if the PEP belongs under one shown at the :ref:`topic-index`.
  Most PEPs don't.

- Post-History can be 'Pending' for now; you'll add dates and corresponding links
  to this header each time you post your PEP to the designated discussion forum
  (and update the Discussions-To header with said link, as above).
  For each thread, use the date (in the ``DD-MMM-YYYY`` format) as the
  linked text, and insert the URLs inline as anonymous reST `hyperlinks`_,
  with commas in between each posting.

  If you posted threads for your PEP on August 14, 2001 and September 3, 2001,
  the Post-History header would look like, e.g.:

  .. code-block:: email

      Post-History: `14-Aug-2001 <https://www.example.com/thread_1>`__,
                    `03-Sept-2001 <https://www.example.com/thread_2>`__

  You should add the new dates/links here as soon as you post a
  new discussion thread.

- Add a Replaces header if your PEP obsoletes an earlier PEP.  The
  value of this header is the number of the PEP that your new PEP is
  replacing.  Only add this header if the older PEP is in "final"
  form, i.e. is either Accepted, Final, or Rejected.  You aren't
  replacing an older open PEP if you're submitting a competing idea.

- Now write your Abstract, Rationale, and other content for your PEP,
  replacing all this gobbledygook with your own text. Be sure to
  adhere to the format guidelines below, specifically on the
  prohibition of tab characters and the indentation requirements.
  See "Suggested Sections" below for a template of sections to include.

- Update your Footnotes section, listing any footnotes and
  non-inline link targets referenced by the text.

- Run ``./build.py`` to ensure the PEP is rendered without errors,
  and check that the output in :file:`build/pep-{NNNN}.html` looks as you intend.

- Create a pull request against the `PEPs repository`_.

For reference, here are all of the possible header fields (everything
in brackets should either be replaced or have the field removed if
it has a leading ``*`` marking it as optional and it does not apply to
your PEP):

.. code-block:: email

  PEP: [NNN]
  Title: [...]
  Author: [Full Name <email at example.com>]
  Sponsor: *[Full Name <email at example.com>]
  PEP-Delegate:
  Discussions-To: [URL]
  Status: Draft
  Type: [Standards Track | Informational | Process]
  Topic: *[Governance | Packaging | Release | Typing]
  Requires: *[NNN]
  Created: [DD-MMM-YYYY]
  Python-Version: *[M.N]
  Post-History: [`DD-MMM-YYYY <URL>`__]
  Replaces: *[NNN]
  Superseded-By: *[NNN]
  Resolution:


ReStructuredText PEP Formatting Requirements
============================================

The following is a PEP-specific summary of reStructuredText syntax.
For the sake of simplicity and brevity, much detail is omitted.  For
more detail, see `Resources`_ below.  `Literal blocks`_ (in which no
markup processing is done) are used for examples throughout, to
illustrate the plaintext markup.


General
-------

Lines should usually not extend past column 79,
excepting URLs and similar circumstances.
Tab characters must never appear in the document at all.


Section Headings
----------------

PEP headings must begin in column zero and the initial letter of each
word must be capitalized as in book titles.  Acronyms should be in all
capitals.  Section titles must be adorned with an underline, a single
repeated punctuation character, which begins in column zero and must
extend at least as far as the right edge of the title text (4
characters minimum).  First-level section titles are underlined with
"=" (equals signs), second-level section titles with "-" (hyphens),
and third-level section titles with "'" (single quotes or
apostrophes).  For example::

    First-Level Title
    =================

    Second-Level Title
    ------------------

    Third-Level Title
    '''''''''''''''''

If there are more than three levels of sections in your PEP, you may
insert overline/underline-adorned titles for the first and second
levels as follows::

    ============================
    First-Level Title (optional)
    ============================

    -----------------------------
    Second-Level Title (optional)
    -----------------------------

    Third-Level Title
    =================

    Fourth-Level Title
    ------------------

    Fifth-Level Title
    '''''''''''''''''

You shouldn't have more than five levels of sections in your PEP.  If
you do, you should consider rewriting it.

You must use two blank lines between the last line of a section's body
and the next section heading.  If a subsection heading immediately
follows a section heading, a single blank line in-between is
sufficient.

The body of each section is not normally indented, although some
constructs do use indentation, as described below.  Blank lines are
used to separate constructs.


Paragraphs
----------

Paragraphs are left-aligned text blocks separated by blank lines.
Paragraphs are not indented unless they are part of an indented
construct (such as a block quote or a list item).


Inline Markup
-------------

Portions of text within paragraphs and other text blocks may be
styled.  For example::

    Text may be marked as *emphasized* (single asterisk markup,
    typically shown in italics) or **strongly emphasized** (double
    asterisks, typically boldface).  ``Inline literals`` (using double
    backquotes) are typically rendered in a monospaced typeface.  No
    further markup recognition is done within the double backquotes,
    so they're safe for any kind of code snippets.


Block Quotes
------------

Block quotes consist of indented body elements.  For example::

    This is a paragraph.

        This is a block quote.

        A block quote may contain many paragraphs.

Block quotes are used to quote extended passages from other sources.
Block quotes may be nested inside other body elements.  Use 4 spaces
per indent level.


Literal Blocks
--------------

..
    In the text below, double backquotes are used to denote inline
    literals.  "``::``" is written so that the colons will appear in a
    monospaced font; the backquotes (``) are markup, not part of the
    text.  See "Inline Markup" above.

    By the way, this is a comment, described in "Comments" below.

Literal blocks are used for code samples and other preformatted text.
To indicate a literal block, preface the indented text block with
"``::``" (two colons), or use the ``.. code-block::`` directive.
Indent the text block by 4 spaces; the literal block continues until the end
of the indentation. For example::

    This is a typical paragraph.  A literal block follows.

    ::

        for a in [5, 4, 3, 2, 1]:  # this is program code, shown as-is
            print(a)
        print("it's...")

"``::``" is also recognized at the end of any paragraph; if not immediately
preceded by whitespace, one colon will remain visible in the final output::

    This is an example::

        Literal block

By default, literal blocks will be syntax-highlighted as Python code.
For specific blocks that contain code or data in other languages/formats,
use the ``.. code-block:: language`` directive, substituting the "short name"
of the appropriate `Pygments lexer <https://pygments.org/docs/lexers/>`_
(or ``text`` to disable highlighting) for ``language``. For example::

    .. code-block:: rst

        An example of the ``rst`` lexer (i.e. *reStructuredText*).

For PEPs that predominantly contain literal blocks of a specific language,
use the ``.. highlight:: language`` directive with the appropriate ``language``
at the top of the PEP body (below the headers and above the Abstract).
All literal blocks will then be treated as that language,
unless specified otherwise in the specific ``.. code-block``. For example::

    .. highlight:: c

    Abstract
    ========

    Here's some C code::

        printf("Hello, World!\n");


Lists
-----

Bullet list items begin with one of "-", "*", or "+" (hyphen,
asterisk, or plus sign), followed by whitespace and the list item
body.  List item bodies must be left-aligned and indented relative to
the bullet; the text immediately after the bullet determines the
indentation.  For example::

    This paragraph is followed by a list.

    * This is the first bullet list item.  The blank line above the
      first list item is required; blank lines between list items
      (such as below this paragraph) are optional.

    * This is the first paragraph in the second item in the list.

      This is the second paragraph in the second item in the list.
      The blank line above this paragraph is required.  The left edge
      of this paragraph lines up with the paragraph above, both
      indented relative to the bullet.

      - This is a sublist.  The bullet lines up with the left edge of
        the text blocks above.  A sublist is a new list so requires a
        blank line above and below.

    * This is the third item of the main list.

    This paragraph is not part of the list.

Enumerated (numbered) list items are similar, but use an enumerator
instead of a bullet.  Enumerators are numbers (1, 2, 3, ...), letters
(A, B, C, ...; uppercase or lowercase), or Roman numerals (i, ii, iii,
iv, ...; uppercase or lowercase), formatted with a period suffix
("1.", "2."), parentheses ("(1)", "(2)"), or a right-parenthesis
suffix ("1)", "2)").  For example::

    1. As with bullet list items, the left edge of paragraphs must
       align.

    2. Each list item may contain multiple paragraphs, sublists, etc.

       This is the second paragraph of the second list item.

       a) Enumerated lists may be nested.
       b) Blank lines may be omitted between list items.

Definition lists are written like this::

    what
        Definition lists associate a term with a definition.

    how
        The term is a one-line phrase, and the definition is one
        or more paragraphs or body elements, indented relative to
        the term.


Tables
------

Simple tables are easy and compact::

    =====  =====  =======
      A      B    A and B
    =====  =====  =======
    False  False  False
    True   False  False
    False  True   False
    True   True   True
    =====  =====  =======

There must be at least two columns in a table (to differentiate from
section titles).  Column spans use underlines of hyphens ("Inputs"
spans the first two columns)::

    =====  =====  ======
       Inputs     Output
    ------------  ------
      A      B    A or B
    =====  =====  ======
    False  False  False
    True   False  True
    False  True   True
    True   True   True
    =====  =====  ======

Text in a first-column cell starts a new row.  No text in the first
column indicates a continuation line; the rest of the cells may
consist of multiple lines.  For example::

    =====  =========================
    col 1  col 2
    =====  =========================
    1      Second column of row 1.
    2      Second column of row 2.
           Second line of paragraph.
    3      - Second column of row 3.

           - Second item in bullet
             list (row 3, column 2).
    =====  =========================


Hyperlinks
----------

When referencing an external web page in the body of a PEP, you should
include the title of the page or a suitable description in the text, with
either an inline hyperlink or a separate explicit target with the URL.
Do not include bare URLs in the body text of the PEP, and use HTTPS
links wherever available.

Hyperlink references use backquotes and a trailing underscore to mark
up the reference text; backquotes are optional if the reference text
is a single word.  For example, to reference a hyperlink target named
``Python website``, you would write:

.. code-block:: rst

    In this paragraph, we refer to the `Python website`_.

If you intend to only reference a link once, and want to define it inline
with the text, insert the link into angle brackets (``<>``) after the text
you want to link, but before the closing backtick, with a space between the
text and the opening backtick. You should also use a double-underscore after
the closing backtick instead of a single one, which makes it an anonymous
reference to avoid conflicting with other target names. For example:

.. code-block:: rst

    Visit the `website <https://www.python.org/>`__ for more.

If you want to use one link multiple places with different linked text,
or want to ensure you don't have to update your link target names when
changing the linked text, include the target name within angle brackets
following the text to link, *with an underscore after the target name
but before the closing angle bracket* (or the link **will not work**).
For example:

.. code-block:: rst

    For further examples, see the `documentation <pydocs_>`_.

An explicit target provides the URL.  Put targets in the Footnotes section
at the end of the PEP, or immediately after the paragraph with the reference.
Hyperlink targets begin with two periods and a space (the "explicit
markup start"), followed by a leading underscore, the reference text,
a colon, and the URL.

.. code-block:: rst

    .. _Python web site: https://www.python.org/
    .. _pydocs: https://docs.python.org/

The reference text and the target text must match (although the match
is case-insensitive and ignores differences in whitespace).  Note that
the underscore trails the reference text but precedes the target text.
If you think of the underscore as a right-pointing arrow, it points
*away* from the reference and *toward* the target.


Internal and PEP/RFC Links
--------------------------

The same mechanism as hyperlinks can be used for internal references.
Every unique section title implicitly defines an internal hyperlink target.
We can make a link to the Abstract section like this:

.. code-block:: rst

    Here is a hyperlink reference to the `Abstract`_ section.  The
    backquotes are optional since the reference text is a single word;
    we can also just write: Abstract_.

To refer to PEPs or RFCs, always use the ``:pep:`` and ``:rfc:`` roles,
never hardcoded URLs.
For example:

.. code-block:: rst

    See :pep:`1` for more information on how to write a PEP,
    and :pep:`the Hyperlink section of PEP 12 <12#hyperlinks>` for how to link.

This renders as:

    See :pep:`1` for more information on how to write a PEP,
    and :pep:`the Hyperlink section of PEP 12 <12#hyperlinks>` for how to link.

PEP numbers in the text are never padded, and there is a space (not a dash)
between "PEP" or "RFC" and the number; the above roles will take care of
that for you.


Footnotes
---------

Footnote references consist of a left square bracket, a label, a
right square bracket, and a trailing underscore.
Instead of a number, use a label of the
form "#word", where "word" is a mnemonic consisting of alphanumerics
plus internal hyphens, underscores, and periods (no whitespace or
other characters are allowed).
For example:

.. code-block:: rst

    Refer to The TeXbook [#TeXbook]_ for more information.

which renders as

    Refer to The TeXbook [#TeXbook]_ for more information.

Whitespace must precede the footnote reference.  Leave a space between
the footnote reference and the preceding word.

Use footnotes for additional notes, explanations and caveats, as well as
for references to books and other sources not readily available online.
Native reST hyperlink targets or inline hyperlinks in the text should be
used in preference to footnotes for including URLs to online resources.

Footnotes begin with ".. " (the explicit
markup start), followed by the footnote marker (no underscores),
followed by the footnote body.  For example:

.. code-block:: rst

    .. [#TeXbook] Donald Knuth's *The TeXbook*, pages 195 and 196.

which renders as

    .. [#TeXbook] Donald Knuth's *The TeXbook*, pages 195 and 196.

Footnotes and footnote references will be numbered automatically, and
the numbers will always match.


Images
------

If your PEP contains a diagram or other graphic, you may include it in the
processed output using the ``image`` directive:

.. code-block:: rst

    .. image:: diagram.png

Any browser-friendly graphics format is possible; SVG or PNG are
preferred for graphics, JPEG for photos and GIF for animations.
Images should be optimised to reduce their file size, and should
be legible in both light and dark mode in the browser.

For accessibility and readers of the source text, you should include
a description of the image and any key information contained within
using the ``:alt:`` option to the ``image`` directive:

.. code-block:: rst

     .. image:: dataflow.png
        :alt: Data flows from the input module, through the "black box"
              module, and finally into (and through) the output module.


Comments
--------

A comment is an indented block of arbitrary text immediately
following an explicit markup start: two periods and whitespace.  Leave
the ".." on a line by itself to ensure that the comment is not
misinterpreted as another explicit markup construct.  Comments are not
visible in the processed document.  For example:

.. code-block:: rst

     ..
        This section should be updated in the final PEP.
        Ensure the date is accurate.


Escaping Mechanism
------------------

reStructuredText uses backslashes ("``\``") to override the special
meaning given to markup characters and get the literal characters
themselves.  To get a literal backslash, use an escaped backslash
("``\\``").  There are two contexts in which backslashes have no
special meaning: `literal blocks`_ and inline literals (see `Inline
Markup`_ above).  In these contexts, no markup recognition is done,
and a single backslash represents a literal backslash, without having
to double up.

If you find that you need to use a backslash in your text, consider
using inline literals or a literal block instead.


Intersphinx
-----------

You can use
`Intersphinx references
<https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html>`_
to other Sphinx sites,
such as the `Python documentation <https://docs.python.org/>`_
`packaging.python.org <https://packaging.python.org/>`_,
and `typing.python.org <https://typing.python.org/>`_,
to easily cross-reference pages, sections and Python/C objects.

For example,
to create a link pointing to a section of the typing docs,
you would write the following::

    :ref:`type expression <typing:type-expression>`


Canonical Documentation
-----------------------

As :pep:`PEP 1 describes <1#pep-maintenance>`,
PEPs are considered historical documents once marked Final,
and their canonical documentation/specification should be moved elsewhere.
To indicate this, use the ``canonical-doc`` directive
or an appropriate subclass:

* ``canonical-pypa-spec`` for packaging standards
* ``canonical-typing-spec`` for typing standards

Add the directive between the headers and the first section of the PEP
(typically the Abstract)
and pass as an argument an Intersphinx reference of the canonical doc/spec
(or if the target is not on a Sphinx site, a `reST hyperlink <Hyperlinks_>`__).

For example,
to create a banner pointing to the :mod:`python:sqlite3` docs,
you would write the following::

    .. canonical-doc:: :mod:`python:sqlite3`

which would generate the banner:

    .. canonical-doc:: :mod:`python:sqlite3`

Or for a PyPA spec,
such as the :ref:`packaging:core-metadata`,
you would use::

    .. canonical-pypa-spec:: :ref:`packaging:core-metadata`

which renders as:

    .. canonical-pypa-spec:: :ref:`packaging:core-metadata`

For a typing PEP that introduces no new runtime objects,
you might use something like the first one of these;
for a typing PEP that introduces a new object to the typing module at runtime,
you might use the second::

   .. canonical-typing-spec:: :ref:`typing:packaging-typed-libraries`
   .. canonical-typing-spec:: :ref:`typing:literal-types` and
                              :py:data:`typing.Literal`

The two render as:

   .. canonical-typing-spec:: :ref:`typing:packaging-typed-libraries`
   .. canonical-typing-spec:: :ref:`typing:literal-types` and
                              :py:data:`typing.Literal`

The argument accepts arbitrary reST,
so you can include multiple linked docs/specs and name them whatever you like,
and you can also include directive content that will be inserted into the text.
The following advanced example::

    .. canonical-doc:: the :ref:`python:sqlite3-connection-objects` and :exc:`python:~sqlite3.DataError` docs

        Also, see the :ref:`Data Persistence docs <persistence>` for other examples.

would render as:

    .. canonical-doc:: the :ref:`python:sqlite3-connection-objects` and :exc:`python:sqlite3.DataError` docs

        Also, see the :ref:`Data Persistence docs <persistence>` for other examples.


Habits to Avoid
===============

Many programmers who are familiar with TeX often write quotation marks
like this:

.. code-block:: text

    `single-quoted' or ``double-quoted''

Backquotes are significant in reStructuredText, so this practice
should be avoided.  For ordinary text, use ordinary 'single-quotes' or
"double-quotes".  For inline literal text (see `Inline Markup`_
above), use double-backquotes::

    ``literal text: in here, anything goes!``


Suggested Sections
==================

Various sections are found to be common across PEPs and are outlined in
:pep:`1`. Those sections are provided here for convenience.

.. _template:

.. include:: pep-0012/pep-NNNN.rst
   :code: rst


Resources
=========

Many other constructs and variations are possible,
both those supported by basic `Docutils <https://docutils.sourceforge.io/>`_
and the extensions added by `Sphinx <https://www.sphinx-doc.org/>`_.

A number of resources are available to learn more about them:

* `Sphinx ReStructuredText Primer
  <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_,
  a gentle but fairly detailed introduction.

* `reStructuredText Markup Specification
  <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html>`_,
  the authoritative, comprehensive documentation of the basic reST syntax,
  directives, roles and more.

* `Sphinx Roles
  <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html>`_
  and `Sphinx Directives
  <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_,
  the extended constructs added by the Sphinx documentation system used to
  render the PEPs to HTML.

If you have questions or require assistance with writing a PEP that the above
resources don't address, ping ``@python/pep-editors`` on GitHub, open an
`issue on the PEPs repository <https://github.com/python/peps/issues>`_
or reach out to a PEP editor directly.


Change History
==============

* `22-Feb-2026 <https://discuss.python.org/t/small-but-useful-change-to-pep-1-12/106250>`_

  * Suggest a new section, headed ``Change History`` to the PEP template, and
    add that section to this PEP.
  * The ``Rationale`` section now comes after the ``Specification`` section.


Copyright
=========

This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.
````

</details>
