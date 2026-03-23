import asyncio
from pydantic_ai import Agent

from input_spec import spec_text
from models import SectionSpec


agent = Agent(
    "openai:gpt-4o-mini",
    output_type=SectionSpec,
    system_prompt=(
        "You are a clinical form schema generator. "
        "Convert the user's textual specification into a valid structured form section. "
        "Return only data that matches the required schema."
        "Use camelCase for field keys and kebab-case for section id."
    ),
    retries=3
)


async def main():
    result = await agent.run(spec_text)

    print("Structured object:")
    print(result.output)

    print("\nJSON output:")
    print(result.output.model_dump_json(indent=2, exclude_none=True, ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(main())