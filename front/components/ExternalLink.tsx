import { Link, Href } from 'expo-router';
import { ComponentProps } from 'react';

// Option 1: The most correct way - use Expo Router's Href type directly
export function ExternalLink({ href, ...rest }: { href: Href } & ComponentProps<typeof Link>) {
  return <Link href={href} {...rest} />;
}

// Option 2: If you need to restrict to specific paths
type AllowedPaths = 
  | "/(tabs)"
  | "/(tabs)/explore"
  | "/(tabs)/profile"
  | "/"
  | `/?${string}`
  | `/#${string}`
  | "/_sitemap"
  | `/_sitemap?${string}`
  | `/_sitemap#${string}`;

export function RestrictedExternalLink({ href, ...rest }: { href: AllowedPaths } & ComponentProps<typeof Link>) {
  return <Link href={href} {...rest} />;
}

// Usage examples:
function ExampleUsage() {
  return (
    <>
      <ExternalLink href="/">Home</ExternalLink>

    </>
  );
}