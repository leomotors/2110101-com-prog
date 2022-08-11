import fs from "node:fs/promises";
import type { DefaultTheme } from "vitepress";

const sidebarItems: DefaultTheme.SidebarItem[] = [];

async function createMd(file: string) {
  const tokens = file.split(".");
  const ext = tokens[tokens.length - 1];

  fs.writeFile(
    `web/grader/${file}.md`,
    `
  # ${file}

  \`\`\`${ext == "hs" ? "haskell" : ext}
  ${(await fs.readFile(`grader/${file}`)).toString().trim()}
  \`\`\`
  `
  );

  sidebarItems.push({
    text: file,
    link: `/grader/${file}`,
  });
}

async function main() {
  const files = await fs.readdir("grader");

  for (const file of files) {
    await createMd(file);
  }

  await fs.writeFile(
    "web/.vitepress/grader.g.ts",
    `
  export default ${JSON.stringify(sidebarItems)};
  `
  );
}

main();
