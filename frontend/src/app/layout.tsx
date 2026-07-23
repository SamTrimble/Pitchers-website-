import type { Metadata } from "next";

import { SessionProvider } from "@/lib/auth/session-provider";
import "./globals.css";

export const metadata: Metadata = {
  title: "AthleteOS Phase 0",
  description: "Foundation scaffold for AthleteOS.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <SessionProvider>{children}</SessionProvider>
      </body>
    </html>
  );
}
