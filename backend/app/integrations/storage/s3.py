from dataclasses import dataclass


@dataclass(slots=True)
class PresignedUpload:
    method: str
    url: str
    object_key: str
    expires_in_seconds: int


class S3ObjectStorageStub:
    def create_presigned_upload(self, *, object_key: str, expires_in_seconds: int = 900) -> PresignedUpload:
        return PresignedUpload(
            method="PUT",
            url=f"https://example-bucket.s3.amazonaws.com/{object_key}",
            object_key=object_key,
            expires_in_seconds=expires_in_seconds,
        )
