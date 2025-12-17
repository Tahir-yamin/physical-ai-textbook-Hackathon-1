import React from 'react';
import ProtectedRoute from '@site/src/components/ProtectedRoute';
import type { WrapperProps } from '@docusaurus/types';
import type DocItemType from '@theme/DocItem';

type Props = WrapperProps<typeof DocItemType>;

export default function DocItemWrapper(props: Props): JSX.Element {
    return (
        <ProtectedRoute>
            <DocItemType {...props} />
        </ProtectedRoute>
    );
}
