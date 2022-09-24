import fs from "node:fs/promises";
import type { DefaultTheme } from "vitepress";

type Builder = (file: string, child: string) => string;

async function createMd(
  file: string,
  folder: string,
  sidebarItems: DefaultTheme.SidebarItem[],
  builder: Builder
) {
  const tokens = file.split(".");
  const ext = tokens[tokens.length - 1];

  fs.writeFile(
    `web/${folder}/${file}.md`,
    builder(
      file,
      `
\`\`\`${ext == "hs" ? "haskell" : ext}
${(await fs.readFile(`${folder}/${file}`)).toString().trim()}
\`\`\`
`
    )
  );

  sidebarItems.push({
    text: file,
    link: `/${folder}/${file}`,
  });
}

async function writeFolder(folderName: string, builder: Builder) {
  const sidebarItems: DefaultTheme.SidebarItem[] = [];
  const files = await fs.readdir(folderName);

  for (const file of files) {
    await createMd(file, folderName, sidebarItems, builder);
  }

  await fs.writeFile(
    `web/.vitepress/${folderName}.g.ts`,
    `
  export default ${JSON.stringify(sidebarItems)};
  `
  );
}

writeFolder(
  "grader",
  (file, child) => `
# ${file}

::: warning
โค้ดกาวมากครับ อย่าลอกเลย 😭😭😭

ทำเองเถอะนะครับ จะได้ทำข้อสอบได้ 🥲🥲🥲
:::

${child}

<!-- @include: ../.vitepress/chad.md -->
`
);

writeFolder(
  "exam",
  (file, child) => `
# ${file}

::: tip
อยากลอกก็ย้อนเวลาไปลอกสิครับ
:::

${child}

<!-- @include: ../.vitepress/chad2.md -->
`
);
