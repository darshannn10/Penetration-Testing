# Image OSINT

## Reverse Image Searching


[<mark style="color:red;">Google images</mark>](https://www.google.com/imghp?hl=en) can be utilized to perform a reverse image search. Simply drag and drop an image into the search to find other instances and similar images to the one uploaded.

Google search operators can be used inline with the image search to further modify the results. For example related URLs can be redacted _"-www -twitter.com -reddit.com"_


[<mark style="color:red;">TinEye</mark>](https://tineye.com) can also be used for reverse image searching. TinEye can also be used with filters and by website / collection filter.



### Resources

**Google Image Search:** [https://images.google.com](https://images.google.com)

**Yandex:** [https://yandex.com](https://yandex.com)

**TinEye:** [https://tineye.com](https://tineye.com)

## Exif Data

### Exiftool

**URL:** [https://github.com/exiftool/exiftool](https://github.com/exiftool/exiftool)

```bash
exiftool <File>
```


### Jeffrey's Image Metadata Viewer

[Jeffrey's Image Metadata Viewer](http://exif.regex.info/exif.cgi), a web based tool can be used to view EXIF information from images. This tool can be used to view information such as what device a picture was taken on and at what time and where.


The same tool links the GPS coordinates from images directly to Google maps so we can see exactly where the image was taken. For investigations the location and time information can be correlated with local CCTV to identify who may have taken the images.

{% hint style="info" %}
Many websites such as Twitter and Facebook will remove many parts of EXIF data from uploaded images in order to help protect end users. An example would be GPS information which could be used by criminals, on social media platforms to identify where a particular person may live.
{% endhint %}

### Resources

**Online EXIF:** [http://exif.regex.info/exif.cgi](http://exif.regex.info/exif.cgi)

**Sample Images:** [https://github.com/ianare/exif-samples](https://github.com/ianare/exif-samples)
