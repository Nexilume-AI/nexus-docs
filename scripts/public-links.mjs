// Product links must use the organization's repository, not a personal fork.
export function assertPublicRepositoryLinks(content) {
  const links = content.matchAll(/https:\/\/github\.com\/([^/\s"'<>]+)\/(nexus(?:-[\w-]+)?)(?=[/\s"'<>?#)]|$)/gi);
  for (const [, owner, repository] of links) {
    if (owner.toLowerCase() !== 'nexilume-ai') {
      throw new Error(`Unexpected public repository owner for ${repository}`);
    }
  }
}
