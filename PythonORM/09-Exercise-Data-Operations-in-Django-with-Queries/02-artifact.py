def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool) -> str:
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )

    return f"The artifact {artifact.name} is {artifact.age} years old!"


def rename_artifact(artifact: Artifact, new_name: str) -> None:

    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()
        
        
def delete_all_artifacts() -> None:
    Artifact.objects.all().delete()