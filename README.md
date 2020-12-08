Parler's unofficial API with all endpoints present in their iOS app as of 08/12/2020.

For the most part undocumented, but the error responses are already quite descriptive.

Any endpoint starting with `/v3/` is protobuf-based. The .proto files can be found elsewhere.

Use it to solve fun mysteries such as:

- Is my dad on Parler?
- Who was on Parler before it first started gaining popularity when Candice Owens tweeted about in December 2018?
- Which users have administration and moderation rights? (hint: `(interactions >> 5) & 1` = moderator, `(interactions >> 6) & 1` = admin)
- What exactly is an "integration partner", and which media entities currently are they?
- If Parler is really yet to come up with a business model for how to make money, then what exactly is a Campaign Promoter Management Network?
- How does the payment integration that lets users be financially rewarded for their posts play into that?
- Whenever John Matze says "influencer marketing" should I really be hearing, "we've created a pavlovian conditioning machine that rewards already gullible people for organically spreading disinformation campaigns"? (most likely)
- Is Parler really the world's most secure social network? (no)

I rushed this just so I didn't have to stare at ghidra anymore. There might be bugs/typos. Patches welcome.

### Usage ###

```python
from parler import Parler

parler = Parler('mst_cookie', 'jst_cookie') # You can also just do the login flow.
parler.user_api.get_profile_for_user(params={'id': 'a078092e6e2df507bfd12db4710202ab'})
```

### Disclaimer ###

Digital Millennium Copyright Act (DMCA) USC § 1201 (f) states:

A person who has lawfully obtained the right to use a copy of a computer program may circumvent a technological measure that effectively controls access to a particular portion of that program for the sole purpose of identifying and analyzing those elements of the program that are necessary to achieve interoperability of an independently created computer program with other programs, and that have not previously been readily available to the person engaging in the circumvention, to the extent any such acts of identification and analysis do not constitute infringement under this title.
