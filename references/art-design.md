# Art & Design

## ColorMagic
`GET https://colormagic.app/api/_payload.json?0db3f926-1e79-4c1a-8961-202cb53807e2`
Fields: data, prerenderedAt. Limit: unknown. Fallback: `dummyimage`.

## DiceBear
`GET https://api.dicebear.com/10.x/lorelei/svg?seed=Felix`
Fields: xml. Limit: unknown. Fallback: `colormagic`.

## DummyImage
`GET https://dummyimage.com/v1`
Fields: binary. Limit: unknown. Fallback: `icons8`.

## DummyImage
`GET https://dummyimage.com/v2`
Fields: binary. Limit: unknown. Fallback: `colormagic`.

## Icons8
`GET https://img.icons8.com/api`
Fields: binary. Limit: unknown. Fallback: `lordicon`.

## Lordicon
`GET https://media.lordicon.com/assets/icons/main/mobile-menu.json`
Fields: v, fr, ip, op, w, h, nm, ddd. Limit: unknown. Fallback: `metropolitan-museum-of-art`.

## Metmuseum
`GET https://collectionapi.metmuseum.org/public/collection/v1/objects/436535`
Fields: objectID, isHighlight, accessionNumber, accessionYear, isPublicDomain, primaryImage, primaryImageSmall, additionalImages. Limit: unknown. Fallback: `colormagic`.

## Metropolitan Museum of Art
`GET https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds=1`
Fields: total, objectIDs. Limit: unknown. Fallback: `dicebear`.
