"use client";

import React from 'react';
import { usePathname } from 'next/navigation';
import Link from 'next/link';
import Image from 'next/image';
import { Button } from '@/components/ui/button';

interface AuthLayoutProps {
    children: React.ReactNode;
}

const AuthLayout = ({ children }: AuthLayoutProps) => {
    const pathname = usePathname();
    const isSignIn = pathname === '/sign-in';

    return (
        <main className='bg-neutral-100 min-h-screen'>
            <div className='mx-auto max-width-2xl p-4'>
                <nav className='flex justify-between items-center'>
                    <Image src='/logo.svg' alt='logo' width={52} height={56} />
                    <Button asChild variant="secondary">
                        <Link href={isSignIn ? '/sign-up' : '/sign-in'}>
                            {isSignIn ? 'Sign Up' : 'Login'}
                        </Link>
                    </Button>
                </nav>
                <div className='flex flex-col items-center justify-center pt-4 md:pt-14'>
                    {children}
                </div>
            </div>
        </main>
    );
}

export default AuthLayout;