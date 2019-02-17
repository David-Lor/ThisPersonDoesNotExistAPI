# ThisPersonDoesNotExistAPI

Unofficial "API" for the [ThisPersonDoesNotExist](https://thispersondoesnotexist.com/) website.

## What is ThisPersonDoesNotExist?

A page that returns a JPEG picture of a person that does not exist, because it has been generated using an AI.
When opening the webpage, a image is returned directly, and refreshing the page will return a new image (although they can be repeated because the repository is limited and images are not generated on real time).

Some articles about it:
- [This Person Does Not Exist - Computer generated people Refresh to get a new one | Product Hunt](https://www.producthunt.com/posts/this-person-does-not-exist)
- [Thispersondoesnotexist.com is face-generating AI at its creepiest](https://thenextweb.com/artificial-intelligence/2019/02/13/thispersondoesnotexist-com-is-face-generating-ai-at-its-creepiest/)

## Why creating/using an "API"?

Why not? Use your imagination!

## Requirements

* Python 3.6
* requests library
* free time

## Usage

### Get a person using function

```python
from thispersondoesnotexist import get_online_person
picture = get_online_person()  # bytes representation of the image

# Save to a file
from thispersondoesnotexist import save_picture
save_picture(picture, "a_beautiful_person.jpeg")
# If no filename is provided, one will be generated using the checksum of the picture
save_picture(picture)

```

### Get a person using class

```python
from thispersondoesnotexist import Person
# Initialize with True to automatically get a person from the webpage
person = Person(fetch_online=True)

# Save to a file
person.save("a_beautiful_person.jpeg")
# If no filename is provided, one will be generated using the checksum of the picture
person.save()

```

### Generate checksums

This can be useful if you want to create a scraper of fictional persons. You would be calling the methods to get random pictures, and to avoid repeating them, you can use their checksum - or just save with the auto-generated filename.

```python
from thispersondoesnotexist import get_online_person, get_checksum_from_picture, Person

# Using object
person = Person(fetch_online=True)
checksum = person.get_checksum("md5")

# Using function
picture = get_online_person()
checksum2 = get_checksum_from_picture(picture)  # Method is optional, defaults to "md5"

```
